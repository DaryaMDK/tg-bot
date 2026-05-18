from aiogram import Router
from aiogram.types import Message

from app.keyboards.menu import nav_menu

router = Router()


@router.message()
async def fallback_handler(message: Message):
    await message.answer(
        "Я пока не понимаю такие сообщения 🙂", reply_markup=nav_menu()
    )
