import asyncio
import pytest
import pytest_asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.database import Base
from settings import TEST_DATABASE_URL

engine_test = create_async_engine(TEST_DATABASE_URL, echo=False)

async_session = async_sessionmaker(engine_test, expire_on_commit=False)


@pytest_asyncio.fixture(loop_scope="module")
async def init():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(loop_scope="module")
async def session(init, mocker):
    async with async_session() as session:
        mocker.patch(
            "src.repositories.news.async_session_factory", return_value=session
        )
        yield session
