from fastapi import APIRouter, status
from lib.models import models
from lib.scheduler import telegram_scheduler_object

notification_router = APIRouter(prefix='/notifications')

@notification_router.post('/{deed_id}/', status_code=status.HTTP_201_CREATED)
def add_notification(deed_id: int, add_notificattor: models.AddNotificator):
    telegram_scheduler_object.add_task(
        task_id=deed_id,
        user_id=add_notificattor.telegram_id,
        task_name=add_notificattor.deed_name,
        task_time=add_notificattor.deed_time
    )

@notification_router.delete('/{deed_id}/', status_code=status.HTTP_200_OK)
def delete_notification(deed_id: int):
    telegram_scheduler_object.delete_task(deed_id)
