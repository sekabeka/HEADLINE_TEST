import asyncio
import aiogram.utils.formatting as fm

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger

from src.repositories.news import NewsRepository
from src.bot import bot

async def send_news():
    repository = NewsRepository()
    async for news, user, source in repository.news_for_messages():
        try:
            await bot.send_message(
                chat_id=user.tg_id,
                **fm.as_section(
                    fm.Italic(news.title),
                    "\n",
                    fm.as_key_value(
                        fm.Bold("Источник"),
                        fm.TextLink(
                            source.url.replace("https://", ""), url=news.url
                        ),
                    ),
                ).as_kwargs()
            )
            logger.info(f"[SCHEDULER] send news to {user.tg_id}")
        except Exception as e:
            logger.error(f"{e}: user_tg_id: {user.tg_id}")

        await asyncio.sleep(1)

scheduler = AsyncIOScheduler()
scheduler.add_job(send_news, "interval", seconds=30)
