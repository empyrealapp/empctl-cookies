from pathlib import Path

def load_prompt(name: str) -> str:
    return Path(__file__).parent.joinpath(f"{name}.md").read_text()


MAIN_PROMPT = load_prompt("main")


__all__ = ["MAIN_PROMPT"]
