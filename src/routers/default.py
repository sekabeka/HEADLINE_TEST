import asyncio
import aiogram.utils.formatting as fm

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram_dialog import DialogManager, StartMode

from loguru import logger

from src.routers.dialogs import router as dialogs_router
from src.states import *

from src.repositories.users import create_user
from src.repositories.news import NewsRepository

router = Router()
router.include_router(dialogs_router)


@router.message(Command("start"))
async def start_handler(message: types.Message, dialog_manager: DialogManager):
    user_id = message.from_user.id
    await create_user(user_id)
    logger.info(f"start dialog. user_id:{user_id}")
    await dialog_manager.start(state=StartSG.menu, mode=StartMode.RESET_STACK)


@router.message(Command("subscriptions"))
async def subs_handler(message: types.Message, dialog_manager: DialogManager):
    user_id = message.from_user.id
    logger.info(f"subscription dialog. user_id:{user_id}")
    await dialog_manager.start(
        state=SubscriptionSG.view,
        mode=StartMode.RESET_STACK,
    )


@router.message(Command("news"))
async def request_news_handler(message: types.Message, dialog_manager: DialogManager):
    repository = NewsRepository()
    news_list = sorted(
        await repository.extract_news(), key=lambda obj: obj.id, reverse=True
    )
    user_id = message.from_user.id
    if news_list:
        logger.info(f"send news. user_id:{user_id}")
        for news in news_list[:10]:
            await message.answer(
                **fm.as_section(
                    fm.Italic(news.title),
                    "\n",
                    fm.as_key_value(
                        fm.Bold("Источник"),
                        fm.TextLink(
                            news.source.url.replace("https://", "").replace('/', ""), url=news.url
                        ),
                    ),
                ).as_kwargs()
            )
            await asyncio.sleep(1)
    else:
        await message.answer("OOps. Новостей не найдено(")
