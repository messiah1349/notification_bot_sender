from datetime import datetime
from pydantic import BaseModel

class AddNotificator(BaseModel):
    telegram_id: int
    deed_name: str
    deed_time: datetime
