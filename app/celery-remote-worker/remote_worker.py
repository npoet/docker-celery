from celery import Celery
import os
from time import sleep

# Celery app using RabbitMQ in docker container at port 4369
celery_app = Celery(
    'celery-api-worker',
    backend=os.environ['CELERY_BACKEND'],
    broker=os.environ['CELERY_BROKER_URL']
)


@celery_app.task(name='calculate', track_started=True)
def calculate(task_id, duration):     # TODO: test
    """
    "calculate" by waiting 'duration' seconds assoc with task_id
    :param task_id: item_id from db, int ascending
    :param duration:
    :return: duration in seconds
    """
    # 'calculate' for duration seconds
    sleep(duration)
    return task_id, duration
