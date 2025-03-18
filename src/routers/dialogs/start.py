from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import (
    Const,
    Multi,
)
from aiogram_dialog.widgets.kbd import (
    Group,
)

from src.buttons import (
    BUTTON_TO_SUBSCRIPTIONS,
)
from src.states import *


dialog = Dialog(
    Window(
        Const("Вот основные функции!"),
        Multi(
            Const("/news - получить последние 10 новостей"),
            Const("/subscriptions - посмотреть подписки или кнопка ниже"),
            Const("/start - это сообщение"),
        ),
        Group(
            BUTTON_TO_SUBSCRIPTIONS,
            width=2
        ),
        state=StartSG.menu,
    )
)
