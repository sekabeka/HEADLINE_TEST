from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database import async_session_factory
from src.models import User


async def create_user(user_id):
    async with async_session_factory() as session:
        query = select(User).where(User.tg_id == user_id)

        user = (await session.execute(query)).scalars().first()
        if user is None:
            user = User(tg_id=user_id)
            session.add(user)
            await session.commit()

        return user
