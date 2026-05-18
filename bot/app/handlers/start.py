from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from app.keyboards.menu import main_menu
from app.texts.messages import home_text

router = Router()


@router.message(CommandStart())
@router.message(F.text == "Меню")
async def cmd_start(message: Message):
    await message.answer(home_text(), reply_markup=main_menu())


@router.message(F.text == "Спрятать меню")
async def hide_menu(message: Message):
    await message.answer(
        "✅ Меню скрыто. Используйте /start чтобы открыть снова.",
        reply_markup=ReplyKeyboardRemove(),
    )
