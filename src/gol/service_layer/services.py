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


def current_week_actions(uow: AbstractUnitOfWork):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    with uow:
        actions = uow.actions.list(
            start_of_week,
            end_of_week
        )
        return actions


def calc_last_week_total_score(uow: AbstractUnitOfWork):
    actions = current_week_actions(uow)
    total = 0
    for action in actions:
        total += action.score
    return total

