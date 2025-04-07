import asyncio

from emp_agents import AgentBase, AssistantMessage, UserMessage
from emp_agents.providers import OpenAIProvider, OpenAIModelType

from {{ cookiecutter.project_slug }}.prompts import MAIN_PROMPT
from {{ cookiecutter.project_slug }}.services import message_service, user_service

agent = AgentBase(
    provider=OpenAIProvider(default_model=OpenAIModelType.gpt4o),
    prompt=MAIN_PROMPT,
    sync_tools=True,
)

async def amain():
    """Main entry point for {{ cookiecutter.project_name }}"""
    while True:
        user_name = input("Input Name: ")
        if user_name == "{{ cookiecutter.project_slug }}":
            print("Try again, name is reserved")
            user_name = "{{ cookiecutter.project_name }}"
        else:
            break

    user = user_service.get_or_create(username=user_name)
    agent_db_user = user_service.get_or_create(username="{{ cookiecutter.project_slug }}")

    message_history = message_service.get_latest_message([user.id, agent_db_user.id])
    messages = [
        UserMessage(content=message.content)
        if message.user_id == user.id else AssistantMessage(content=message.content)
        for message in message_history
    ]
    agent.conversation.set_history(messages)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q", "bye"]:
            response = await agent.answer("I am leaving, send me a friendly goodbye!")
            print(f"Agent: {response}")
            break
        message_service.add_message(user_input, user.id)
        agent.add_message(UserMessage(content=user_input))
        response = await agent.complete()
        message_service.add_message(response, agent_db_user.id)
        print(f"Agent: {response}")

        if len(agent.conversation.get_history()) > 10:
            message_history = message_service.get_latest_message([user.id, agent_db_user.id])
            messages = [
                UserMessage(content=message.content)
                if message.user_id == user.id else AssistantMessage(content=message.content)
                for message in message_history
            ]
            agent.conversation.set_history(messages)

def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
