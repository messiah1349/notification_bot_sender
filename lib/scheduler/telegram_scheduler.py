from telegram import Message
from telegram.error import TelegramError
import logging

from lib.scheduler.task_scheduler import TaskScheduler
from lib.sender.telegram_sender import send_telegram_message

logger = logging.getLogger(__name__)

class TelegramScheduler(TaskScheduler):
    async def send_message(self, user_id: int, message_text: str, deed_id: int) -> Message:
        try:
            await send_telegram_message(
                deed_id=deed_id, 
                chat_id=user_id,
                text=message_text
            )
            logger.debug(f"message for {deed_id=} was sent")
        except TelegramError as te:
            logger.error(f"could not send message for {deed_id=} error_text: {te}")
