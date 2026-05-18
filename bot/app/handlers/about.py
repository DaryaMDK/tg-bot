from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.menu import nav_menu
from app.texts.messages import about_text

router = Router()


@router.message(F.text == "Обо мне")
@router.message(Command("about"))
async def show_about(message: Message):
    await message.answer(about_text(), reply_markup=nav_menu())
