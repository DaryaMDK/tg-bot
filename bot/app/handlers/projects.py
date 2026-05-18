from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.menu import nav_menu
from app.texts.messages import projects_text

router = Router()

@router.message(F.text == "Проекты")
@router.message(Command("projects"))
async def show_projects(message: Message):
    await message.answer(
        projects_text(),
        reply_markup=nav_menu()
    )