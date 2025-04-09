from pathlib import Path

def load_prompt(name: str) -> str:
    return Path(__file__).parent.joinpath(f"{name}.md").read_text()


GROUP_CHAT_PROMPT = load_prompt("group")
PRIVATE_CHAT_PROMPT = load_prompt("private")

__all__ = ["GROUP_CHAT_PROMPT", "PRIVATE_CHAT_PROMPT"]
