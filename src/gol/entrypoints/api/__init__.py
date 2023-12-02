from typing import List

from fastapi import FastAPI

from gol.service_layer import services
from gol.service_layer.uow import SQLModelUnitOfWork
from gol.presentation.schemas import ActionSchema, AddActionSchema

app = FastAPI()


@app.post('/add-action', response_model=ActionSchema)
def add_action(action: AddActionSchema):
    uow = SQLModelUnitOfWork()
    action = services.add_action(action.title, action.score, uow)
    return action


@app.get('/weekly-actions', response_model=List[ActionSchema])
def weekly_actions():
    uow = SQLModelUnitOfWork()
    actions = services.weekly_actions(uow)
    return actions

