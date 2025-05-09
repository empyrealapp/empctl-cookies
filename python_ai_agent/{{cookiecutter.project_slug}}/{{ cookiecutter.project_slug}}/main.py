from typing import Annotated
from typing_extensions import Doc

from pydantic import BaseModel
from emp_agents import AgentBase
from emp_agents.providers import OpenAIProvider, OpenAIModelType
from emp_hooks.handlers.telegram import Update, ContextTypes, filters, on_message
from emp_hooks import hooks

from {{ cookiecutter.project_slug }}.prompts import prompts
from {{ cookiecutter.project_slug }}.services import chat_service, message_service, user_service, session
from {{ cookiecutter.project_slug }}.tools import TOOLS
from {{ cookiecutter.project_slug }}.logger import logger

class ResponseFormat(BaseModel):
    content: Annotated[str | None, Doc("The response to the user's message, or None if the user should not respond")]
    should_respond: Annotated[bool, Doc("Whether the agent should respond to the user's message")]


@on_message(filter=filters.TEXT & ~filters.COMMAND)
async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Main entry point for {{ cookiecutter.project_name }}"""
    bot_user = user_service.load_bot(context)

    if not (update.message and update.message.from_user):
        return

    logger.info(f"Received message from {update.message.from_user.username}: {update.message.text}")

    prompt = prompts.load(update, context)
    agent = AgentBase(
        prompt=prompt,
        provider=OpenAIProvider(
            default_model=OpenAIModelType.gpt4o,
        ),
        tools=TOOLS,
    )

    # add user and message to database
    chat = chat_service.store_chat(update.message)
    db_user = user_service.store_user(update.message.from_user)
    message_service.add_message(chat, db_user, update.message)

    # create response using conversation history
    response = await agent.answer(
        "\n".join(
            f"{message.user.username}: {message.text}"
            for message in message_service.get_latest_message(chat.id)
        ),
        response_format=ResponseFormat,
    )

    # if agent has something to say, send it
    if response.should_respond and response.content:
        logger.info(f"Sending response to {update.message.from_user.username}: {response.content}")
        response_msg = await update.message.reply_text(response.content)
        message_service.add_message(chat, bot_user, response_msg)
    else:
        logger.info(f"No response from {update.message.from_user.username}")


def main() -> None:
    try:
        hooks.run_forever()
    finally:
        session.close()


if __name__ == "__main__":
    main()
