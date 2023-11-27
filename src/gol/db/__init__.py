from sqlmodel import Session, SQLModel, create_engine

from gol import config
from gol.db.actions import Action

engine = create_engine(config.get_postgres_uri())

SQLModel.metadata.create_all(engine)

