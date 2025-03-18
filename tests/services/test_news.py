import pytest
import pytest_asyncio
from sqlalchemy import select

from src.models import Source, News
from src.repositories.news import NewsRepository


@pytest.mark.asyncio
class TestNewsRepository:
    async def test_extract_news(self, session):
        source = Source(title="some_title", url="some_url")
        news = [
            News(title="some_news_1", url="some_news_url"),
            News(title="some_news_2", url="some_news_url"),
            News(title="some_news_3", url="some_news_url"),
        ]
        source.news = news
        session.add(source)
        await session.commit()

        # Test the repository
        news_repository = NewsRepository(source.id)
        _news = await news_repository.extract_news()
        assert len(news) == len(_news)
        assert news == _news

        # Add another source and news
        other_source = Source(title="some_title2", url="some_url")
        other_news = News(title="some_title4", url="some_news_url")
        other_source.news.append(other_news)
        session.add(other_source)
        await session.commit()

        # Test retrieving all news
        _news = await NewsRepository().extract_news()
        assert len(_news) == 4

    async def test_update_news(self, session):
        # Create a source and initial news
        source = Source(title="some_title_1", url="some_url_1")
        news = [
            News(title="some_news_1", url="some_news_url_1"),
            News(title="some_news_2", url="some_news_url_2"),
        ]
        source.news = news
        session.add(source)
        await session.commit()

        # New news data to update
        news_list = [
            {"title": "some_news_1", "url": "some_news_url_1"},
            {"title": "news_not_in_database", "url": "some_url"},
        ]

        # Test the repository
        news_repository = NewsRepository(source.id)
        await news_repository.update_news(news_list)

        # Verify the updated news
        query = select(News)
        result = await session.execute(query)
        _news = result.scalars().all()

        assert len(_news) == 3

    async def test_1(self, session):
        assert 1 == 1

    async def test_2(self, session):
        assert 1 == 1
