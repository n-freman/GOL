from datetime import datetime

from pydantic import BaseModel


class ActionSchema(BaseModel):
    title: str
    score: float
    date_added: datetime


class AddActionSchema(BaseModel):
    title: str
    score: float

