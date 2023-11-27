from typing import Self

from gol.adapters.abstract import AbstractAdapter
from gol.db import Action


class ActionsAdapter(AbstractAdapter):
    
    def add(
        self: Self,
        title: str,
        score: float
    ) -> Action:
        action = Action(title=title, score=score)
        self.session.add(action)
        return action

