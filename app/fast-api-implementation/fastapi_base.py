from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI app declaration
API_app = FastAPI()


class TaskItem(BaseModel):
    """
    Item class for receiving tasks via POST request
    """
    item_id: int
    duration: int


class IDItem(BaseModel):
    """
    Item class for receiving ID via POST request
    """
    task_id: str
