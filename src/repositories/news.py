from sqlalchemy import select, join
from sqlalchemy.orm import joinedload, subqueryload

from src.database import async_session_factory
from src.models import Source, News, User, subscription_table


class NewsRepository:
    def __init__(self, source_id=None):
        self.source_id = source_id

    async def extract_news(self):
        async with async_session_factory() as session:
            if self.source_id is not None:
                # Fetch news for a specific source
                source = await session.get(
                    Source, self.source_id, options=[joinedload(Source.news)]
                )
                return source.news if source else []
            else:
                # Fetch all news
                query = select(News).options(joinedload(News.source))
                result = await session.execute(query)
                return result.scalars().unique().all()

    async def update_news(self, news_list):
        existing_news = await self.extract_news()

        existing_urls = [news.url for news in existing_news]
        async with async_session_factory() as session:
            for news_data in news_list:
                news_url = news_data["url"]
                if news_url not in existing_urls:
                    session.add(News(**news_data, source_id=self.source_id))

            await session.commit()

    @staticmethod
    async def news_for_messages():
        async with async_session_factory() as session:
            stmt = (
                select(
                    News,
                    User,
                    Source
                )
                .join(News.source)
                .join(Source.users)
                .where(News.was_sent == False)
            )
            for news, user, source in (await session.execute(stmt)):
                yield news, user, source
                news.was_sent = True

            await session.commit()

    @staticmethod
    async def on_startup():
        async with async_session_factory() as session:
            news_list = (
                (await session.scalars(
                    select(News)
                    .where(News.was_sent == False)
                ))
                .all()
            )
            for news in news_list:
                news.was_sent = True

            await session.commit()