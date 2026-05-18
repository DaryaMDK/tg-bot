from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.menu import nav_menu
from app.texts.messages import contacts_text

router = Router()

@router.message(F.text == "Контакты")
@router.message(Command("contacts"))
async def show_contacts(message: Message):
    await message.answer(
        contacts_text(),
        reply_markup=nav_menu()
    )