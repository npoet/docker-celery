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
def calculate(duration):
    """
    "calculate" by waiting 'duration' seconds assoc with task_id
    :param duration: time in seconds to 'calculate' long-running task
    :return: duration in seconds
    """
    sleep(duration)
    return duration
