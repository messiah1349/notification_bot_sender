from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class TaskScheduler(ABC):

    def __init__(self):
        self.schedule = AsyncIOScheduler(daemon=True)
        
    def __repr__(self) -> str:
        return str(self.schedule)

    @abstractmethod
    async def send_message(self, user_id: int, message_text: str, *args, **kwargs):
        raise NotImplementedError

    def add_task(self, task_id: str, user_id: int, task_name: str, task_time: datetime):
        
        self.schedule.add_job(
            self.send_message, 
            'date', 
            run_date=task_time, 
            kwargs={
                "user_id": user_id,
                "message_text": task_name,
                "deed_id": task_id
            },
            id=str(task_id), 
            replace_existing=True
        )
        logger.debug(f"added job {task_name=} with {task_id=} at {task_time=}")

    def delete_task(self, task_id: str):
        self.schedule.remove_job(task_id)
        logger.debug(f"removed job {task_id=}")

    def start_scheduling(self):
        self.schedule.start()
        logger.info("scheduler started")

