from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    telegram_token: str = os.environ.get(
        'NOTIFICATION_BOT_SENDER_TOKEN', 
        '214139458:AAH8UGU0PW3vUE1lRz-gjXnlB6TroUvpfUk'
    )

settings = Settings()