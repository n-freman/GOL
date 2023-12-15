from datetime import datetime
from typing import List

from pydantic import BaseModel


class ActionSchema(BaseModel):
    title: str
    score: float
    date_added: datetime


class AddActionSchema(BaseModel):
    title: str
    score: float


class ActionListResponseSchema(BaseModel):
    actions: List[ActionSchema]
    total_score: float

