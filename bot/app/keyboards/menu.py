from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Обо мне"),
             KeyboardButton(text="Проекты")],
            [KeyboardButton(text="Контакты"),
             KeyboardButton(text="Запрос к LLM")],
            [KeyboardButton(text="Спрятать меню")]
        ],
        resize_keyboard=True
    )

def nav_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Меню")]
        ],
        resize_keyboard=True
    )

def llm_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Меню"), KeyboardButton(text="exit")]
        ],
        resize_keyboard=True
    )

def remove_menu():
    return ReplyKeyboardRemove()