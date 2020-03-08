from celery import Celery
import os

# Celery app using RabbitMQ in docker container at port 4369
celery_app = Celery(
    'celery-api-worker',
    backend=os.environ['CELERY_BACKEND'],
    broker=os.environ['CELERY_BROKER_URL']
)
