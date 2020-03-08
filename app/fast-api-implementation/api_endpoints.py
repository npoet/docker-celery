from database import db_connect
import os
import time
from celery.result import AsyncResult
from api_worker import celery_app
from fastapi_base import *


@API_app.get("/")
def root():
    """
    Root endpoint returns a JSON objecting containing valid endpoints and their methods
    :return: JSON object containing valid endpoints
    """
    return {
        "Available Endpoints": [
            {"GET": ["/tasks/status", "/tasks/from_db"]},
            {"POST": "/tasks/receive"},
        ]
    }


@API_app.post("/tasks/receive")
def receive_new_task(item: TaskItem):
    """
    Adds new given task to db and queue
    :param item: item_id and duration
    :return: task_id
    """
    # Add new task to mssql DB
    db_cursor = db_connect().cursor()
    db_cursor.execute(f"INSERT INTO {os.environ['DB_TABLE']} "
                      f"VALUES ({item.item_id}, {item.duration})")

    task_id = str(int((time.time() * 1000)))  # unique task_id from timestamp
    # Add calculation to queue
    celery_app.send_task(name="calculate", task_id=task_id, args=[item.duration])
    return task_id


@API_app.get("/tasks/from_db")
def run_tasks_from_db():    # TODO: test, fix db select statement
    """
    Adds all db tasks to queue, useful for testing
    :return: list of task_id's corresponding to tasks added
    """
    db_cursor = db_connect().cursor()
    result = db_cursor.execute(f"SELECT * FROM {os.environ['DB_TABLE']}")
    tasks = []
    for line in result:
        task_id = int(time.time() * 1000)  # unique task_id from timestamp
        celery_app.send_task(name="calculate", task_id=task_id, args=[line[0]])
        tasks.append(task_id)
    return tasks


@API_app.post("/tasks/status")
def get_status_by_id(task_id: IDItem):
    """
    Checks status of task with given ID
    :param task_id: task_id for given celery task
    :return: boolean, False if task still running, True if completed
    """
    res = AsyncResult(app=celery_app, id=task_id.task_id)
    return res.status
