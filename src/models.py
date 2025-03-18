from datetime import datetime, timezone

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy import String, BIGINT, Text
from sqlalchemy import select, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT

from src.database import async_session_factory, Base

subscription_table = Table(
    "subscription",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("source_id", ForeignKey("source.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BIGINT)
    actions: Mapped[List["Action"]] = relationship(back_populates="user")
    sources: Mapped[List["Source"]] = relationship(
        back_populates="users", secondary=subscription_table
    )


class Action(Base):
    __tablename__ = "action"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="actions")

    action: Mapped[str]
    timestamp: Mapped[float] = mapped_column(default=datetime.now(tz=timezone.utc))

    def __repr__(self):
        return self.action


class Source(Base):
    __tablename__ = "source"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(length=64))
    url: Mapped[str] = mapped_column(String(128))
    news: Mapped[List["News"]] = relationship("News", back_populates="source")
    users: Mapped[List["User"]] = relationship(
        back_populates="sources", secondary=subscription_table
    )


class News(Base):
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    source_id: Mapped[int] = mapped_column(ForeignKey("source.id"))
    source: Mapped[Source] = relationship(back_populates="news")
    url: Mapped[str] = mapped_column(Text)
    was_sent: Mapped[bool] = mapped_column(default=False)
