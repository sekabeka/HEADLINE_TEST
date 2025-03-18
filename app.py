import asyncio
import logging

from aiogram import Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from src.bot import bot
from src.routers.default import router
from src.sources import (
    LENTA,
    NBC,
    RIA,
)
from src.logger import InterceptHandler
from src.scheduler import scheduler
from src.repositories.news import NewsRepository

logging.basicConfig(handlers=[InterceptHandler()], level="INFO", force=True)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

scrapers = [(LENTA, 1), (NBC, 2), (RIA, 3)]

async def run_scrapers():
    for scraper, _id in scrapers:
        asyncio.create_task(scraper(_id).parse())

async def set_commands():
    await bot.set_my_commands(
        commands=[
            BotCommand(
                command="/start",
                description="начало"
            ),
            BotCommand(
                command="/subscriptions",
                description="подписки"
            ),
            BotCommand(
                command="/news",
                description="последние 10 news"
            )
        ]
    )


async def main():
    dp.include_routers(router)
    setup_dialogs(dp)

    await NewsRepository.on_startup()
    await set_commands()

    scheduler.start()

    await run_scrapers()
    await dp.start_polling(bot)


asyncio.run(main())
