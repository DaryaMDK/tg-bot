import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from app.config.settings import BOT_TOKEN
from app.handlers import about, contacts, fallback, llm_chat, projects, start
from app.utils.logger import setup_logger


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(about.router)
    dp.include_router(projects.router)
    dp.include_router(contacts.router)
    dp.include_router(llm_chat.router)
    dp.include_router(fallback.router)

    await bot.delete_webhook(drop_pending_updates=True)

    print("Бот включен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    setup_logger()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен!")
