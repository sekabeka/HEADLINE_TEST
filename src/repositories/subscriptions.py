from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database import async_session_factory
from src.models import User, Source


async def get_user_and_subs(user_id):
    async with async_session_factory() as session:
        query = (
            select(User).options(joinedload(User.sources)).where(User.tg_id == user_id)
        )
        user = (await session.execute(query)).unique().scalars().first()

        sources = (await session.execute(select(Source))).scalars().all()

        lst = []
        for source in sources:
            if source in user.sources:
                lst.append((source.title, source.id, True))
            else:
                lst.append((source.title, source.id, False))
        return lst


async def update_subscriptions(selected_list, user_id):
    async with async_session_factory() as session:
        query = (
            select(User).options(joinedload(User.sources)).where(User.tg_id == user_id)
        )
        user = (await session.execute(query)).unique().scalars().first()
        sources = (await session.execute(select(Source))).scalars().all()

        user.sources = [
            source for source in sources if source.id in list(map(int, selected_list))
        ]

        await session.commit()
