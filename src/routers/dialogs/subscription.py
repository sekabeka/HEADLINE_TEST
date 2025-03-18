import operator

from aiogram_dialog import Window, Dialog, DialogManager

from aiogram_dialog.widgets.kbd import (
    Multiselect,
)
from aiogram_dialog.widgets.text import (
    Const,
    Format,
)

from src.buttons import BUTTON_TO_MENU
from src.states import SubscriptionSG
from src.repositories.subscriptions import (
    get_user_and_subs,
    update_subscriptions,
)


async def getter(**kwargs):
    return {"sources": kwargs["dialog_manager"].dialog_data["sources"]}


async def on_start(_, dialog_manager: DialogManager):
    sources = await get_user_and_subs(dialog_manager.event.from_user.id)
    dialog_manager.dialog_data["sources"] = sources
    for source in sources:
        await dialog_manager.find("sources").set_checked(source[1], source[-1])


async def on_close(_, dialog_manager: DialogManager):
    selected_list = dialog_manager.find("sources").get_checked()
    await update_subscriptions(selected_list, dialog_manager.event.from_user.id)


dialog = Dialog(
    Window(
        Const("📌 отмечены Ваши подписки. Нажмите, чтобы подписаться/отписаться."),
        Multiselect(
            checked_text=Format("{item[0]} 📌"),
            unchecked_text=Format("{item[0]}"),
            id="sources",
            item_id_getter=operator.itemgetter(1),
            items="sources",
        ),
        BUTTON_TO_MENU,
        getter=getter,
        state=SubscriptionSG.view,
    ),
    on_start=on_start,
    on_close=on_close,
)
