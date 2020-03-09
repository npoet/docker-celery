from celery import Celery
import os

# Celery app declaration
celery_app = Celery(
    'celery-api-worker',
    backend=os.environ['CELERY_BACKEND'],
    broker=os.environ['CELERY_BROKER_URL']
)
