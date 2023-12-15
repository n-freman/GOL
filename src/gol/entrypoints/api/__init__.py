from typing import List

from fastapi import FastAPI

from gol.service_layer import services
from gol.service_layer.uow import SQLModelUnitOfWork
from gol.presentation.schemas import (
    ActionSchema, AddActionSchema,
    ActionListResponseSchema
)

app = FastAPI()


@app.post('/add-action', response_model=ActionSchema)
def add_action(action: AddActionSchema):
    uow = SQLModelUnitOfWork()
    action = services.add_action(action.title, action.score, uow)
    return {
        'title': action.title,
        'score': action.score,
        'date_added': action.date_added
    }


@app.get('/weekly-actions', response_model=ActionListResponseSchema) 
def weekly_actions():
    uow = SQLModelUnitOfWork()
    actions = services.weekly_actions(uow)
    total = services.calc_last_week_total_score(uow)
    return {'actions': list(actions), 'total_score': total}

