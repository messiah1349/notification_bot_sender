from fastapi import APIRouter
from lib.models import models
from lib.scheduler import telegram_scheduler_object

notification_router = APIRouter(prefix='/notifications')

@notification_router.post('/{deed_id}/')
def add_notification(deed_id: int, add_notificattor: models.AddNotificator):
    telegram_scheduler_object.add_task(
        task_id=deed_id,
        user_id=add_notificattor.telegram_id,
        task_name=add_notificattor.deed_name,
        task_time=add_notificattor.deed_time
    )

