from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from sqlalchemy.orm import DeclarativeBase

from settings import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL, echo=False)

async_session_factory = async_sessionmaker(
    async_engine, expire_on_commit=False, autoflush=True
)


class Base(DeclarativeBase): ...
