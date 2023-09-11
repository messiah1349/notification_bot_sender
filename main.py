from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

from lib.sender.telegram_sender import send_telegram_message
from lib.routers.notification import notification_router

app = FastAPI()

app.include_router(notification_router)
