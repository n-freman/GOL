from datetime import date, timedelta

from gol.db import Action
from gol.service_layer.uow import AbstractUnitOfWork, SQLModelUnitOfWork


def add_action(
    title: str,
    score: float,
    uow: AbstractUnitOfWork,
) -> Action:
    with uow:
        action = uow.actions.add(
            title=title,
            score=score
        )
        uow.commit()
        return action


def weekly_actions(uow: AbstractUnitOfWork):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    with uow:
        actions = uow.actions.list(
            start_of_week,
            end_of_week
        )
        return actions

