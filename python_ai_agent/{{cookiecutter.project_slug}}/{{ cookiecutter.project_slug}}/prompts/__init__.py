from pathlib import Path

from pydantic import BaseModel, PrivateAttr
from telegram import Update
from telegram.ext import ContextTypes

from emp_hooks.utils.telegram import is_group_chat


def load_prompt(name: str, username: str) -> str:
    text = Path(__file__).parent.joinpath(f"{name}.md").read_text()

    return text.replace("<TG_BOT_USERNAME>", f"@{username.lstrip("@")}")


class TelegramPromptManager(BaseModel):
    _bot_username: str = PrivateAttr(default="assistant")
    _group_chat_prompt: str | None = PrivateAttr(default=None)
    _private_chat_prompt: str | None = PrivateAttr(default=None)

    @property
    def group_chat_prompt(self) -> str:
        if self._group_chat_prompt is None:
            self._group_chat_prompt = load_prompt("group", self._bot_username)
        return self._group_chat_prompt

    @property
    def private_chat_prompt(self) -> str:
        if self._private_chat_prompt is None:
            self._private_chat_prompt = load_prompt("private", self._bot_username)
        return self._private_chat_prompt

    def load(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
        self._bot_username = context.bot.username
        if is_group_chat(update):
            return self.group_chat_prompt
        return self.private_chat_prompt

    def set_bot_username(self, bot_username: str) -> None:
        self._bot_username = bot_username


prompts = TelegramPromptManager()

__all__ = ["prompts"]
