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

