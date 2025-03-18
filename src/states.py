from aiogram.filters.state import State, StatesGroup


class StartSG(StatesGroup):
    menu = State()


class SubscriptionSG(StatesGroup):
    view = State()
