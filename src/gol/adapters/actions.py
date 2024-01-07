from datetime import date
from functools import lru_cache
from typing import List, Self

from gol.adapters.abstract import AbstractAdapter
from gol.db import Action


class ActionsAdapter(AbstractAdapter):

    def add(
        self: Self, title: str,
        score: float
    ) -> Action:
        action = Action(title=title, score=score)
        self.session.add(action)
        return action

    @lru_cache
    def list(
        self: Self, start_date: date,
        end_date: date
    ) -> List[Action]:
        actions = self.session.query(Action).filter(
            (Action.date_added >= start_date)
            & (Action.date_added <= end_date)
        ).order_by(Action.date_added.desc())
        return actions

    def weekly_score(self):
        pass

