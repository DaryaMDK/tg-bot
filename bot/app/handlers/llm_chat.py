import httpx
import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

from app.states.chat_states import ChatStates
from app.services.ollama_client import ask_llm
from app.keyboards.menu import nav_menu, main_menu, llm_menu
from app.utils.message_splitter import split_text

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.text == "Запрос к LLM")
async def start_llm_chat(
        message: Message,
        state: FSMContext
):
    logger.info(f"User {message.from_user.id} started LLM chat")

    await state.set_state(ChatStates.chatting_with_llm)

    await message.answer(
        "🤖 Режим общения с LLM включён.\n"
        "Введите запрос.",
        reply_markup=llm_menu()
    )


@router.message(
    ChatStates.chatting_with_llm,
    F.text
)
async def chat_with_llm(
        message: Message,
):
    try:
        logger.info(f"Sending request to Ollama: {message.text}")
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.TYPING
        )
        answer = await ask_llm(message.text)
        logger.info("Received response from Ollama")

        chunks = split_text(answer)

        for chunk in chunks:
            await message.answer(
                chunk,
                reply_markup=nav_menu()
            )

    except httpx.ConnectError:
        logger.error("Cannot connect to Ollama")
        await message.answer("LLM сервер недоступен.")

    except httpx.ReadTimeout:
        logger.error("Ollama timeout")
        await message.answer("LLM слишком долго отвечает.")

    except httpx.HTTPStatusError as e:
        logger.error(f"Ollama returned status {e.response.status_code}")
        await message.answer("Ошибка LLM сервера.")

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        await message.answer("Непредвиденная ошибка.")


@router.message(
    ChatStates.chatting_with_llm,
    F.text.lower().in_(["меню", "exit", "/exit"])
)

async def exit_llm_chat(
        message: Message,
        state: FSMContext
):
    await state.clear()
    await message.answer("Вы вышли из режима LLM.", reply_markup=main_menu())