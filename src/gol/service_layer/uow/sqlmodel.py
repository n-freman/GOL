from typing import Self

from gol import db
from gol.adapters import AbstractAdapter, ActionsAdapter
from gol.service_layer.uow.abstract import AbstractUnitOfWork


class SQLModelUnitOfWork(AbstractUnitOfWork):

    def __enter__(self):
        self.session = db.Session(db.engine, expire_on_commit=False)
        self.actions = ActionsAdapter(self.session)

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

