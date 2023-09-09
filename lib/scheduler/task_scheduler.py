from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class TaskScheduler(ABC):

    def __init__(self):
        self.schedule = BackgroundScheduler(daemon=True)
        
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
            args=[task_id, user_id, task_name], 
            id=str(task_id), 
            replace_existing=True
        )
        logger.debug(f"added job {task_name=} with {task_id=} at {task_time=}")

    def delete_task(self, task_id: str):
        self.schedule.remove_job(task_id)
        logger.debug(f"remove job {task_id=}")

    def start_scheduling(self):
        self.schedule.start()
        logger.info("scheduler started")

