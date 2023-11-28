from abc import ABC, abstractmethod
from typing import Self

from gol.adapters import AbstractAdapter


class AbstractUnitOfWork(ABC):
    actions: AbstractAdapter

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args) -> None:
        self.rollback()

    def commit(self):
        self._commit()

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

