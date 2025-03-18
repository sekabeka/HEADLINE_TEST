from aiogram import Router

from .subscription import dialog as subs_dialog
from .start import dialog as start_dialog

router = Router()

router.include_routers(
    subs_dialog,
    start_dialog,
)
