import asyncio
from typing import Annotated
from typing_extensions import Doc

from pydantic import BaseModel
from emp_agents import AgentBase
from emp_agents.providers import OpenAIProvider, OpenAIModelType

from {{ cookiecutter.project_slug }}.prompts import prompts
from {{ cookiecutter.project_slug }}.tools import TOOLS

class ResponseFormat(BaseModel):
    content: Annotated[str | None, Doc("The response to the user's message, or None if the user should not respond")]
    should_respond: Annotated[bool, Doc("Whether the agent should respond to the user's message")]


async def _run_local() -> None:
    """Main entry point for {{ cookiecutter.project_name }}"""
    prompt = prompts.group_chat_prompt
    agent = AgentBase(
        prompt=prompt,
        provider=OpenAIProvider(
            default_model=OpenAIModelType.gpt4o,
        ),
        tools=TOOLS,
    )
    await agent.run()


def run_local() -> None:
    asyncio.run(_run_local())


if __name__ == "__main__":
    run_local()
