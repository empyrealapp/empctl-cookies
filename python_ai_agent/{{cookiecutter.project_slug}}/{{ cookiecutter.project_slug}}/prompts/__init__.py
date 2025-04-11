import os
from pathlib import Path


def load_prompt(name: str) -> str:
    text = Path(__file__).parent.joinpath(f"{name}.md").read_text()
    bot_username = os.getenv("TG_BOT_USERNAME", "@empcloud_demo_bot")

    return text.replace("<TG_BOT_USERNAME>", f"@{bot_username}")


GROUP_CHAT_PROMPT = load_prompt("group")
PRIVATE_CHAT_PROMPT = load_prompt("private")

__all__ = ["GROUP_CHAT_PROMPT", "PRIVATE_CHAT_PROMPT"]
