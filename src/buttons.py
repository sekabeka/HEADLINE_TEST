from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Start

from src.states import *


async def on_click(query, button, dialog_manager):
    await dialog_manager.done()


BUTTON_TO_SUBSCRIPTIONS = Start(
    text=Const("Подписки"), id="subscriptions", state=SubscriptionSG.view
)

BUTTON_TO_MENU = Start(
    text=Const("К меню"), id="menu", state=StartSG.menu, on_click=on_click
)

