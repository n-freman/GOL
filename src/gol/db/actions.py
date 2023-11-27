from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlmodel import TIMESTAMP, Column, Field, SQLModel, text


class Action(SQLModel, table=True):
    id: Optional[str] = Field(
        default_factory=uuid4,
        primary_key=True
    )
    title: str
    score: float
    date_added: Optional[datetime] = Field(
        default_factory=datetime.now,
    )
    date_edited: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP")
    ))

