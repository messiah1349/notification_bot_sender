from telegram import Bot

from core.config import settings
from lib.sender.keyboards import get_inline_deed_after_notify


async def send_telegram_message(deed_id: int, chat_id: int, text: str):
    async with Bot(token=settings.telegram_token) as bot:
        keyboard = get_inline_deed_after_notify(deed_id)
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=keyboard
        )
