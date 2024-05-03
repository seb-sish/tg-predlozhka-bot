from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from utils import InMessageFilter
from keyboards import kb_start, kb_categories
import asyncio

from utils import post
from config import Config

main_router = Router()
main_router.message.filter(F.chat.type.in_({"private"}))
class offerNews(StatesGroup):
    name = State()
    category = State()
    text = State()

@main_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Здравствуйте! Здесь вы можете предложить новость, для этого нажмите на кнопку ниже!", 
                         reply_markup=kb_start)

@main_router.message(F.text == "Предложить новость")
async def offerNews_handler(message: Message, state: FSMContext):
    await state.set_state(offerNews.name)
    await message.answer(
        "Укажите своё имя: ",
        reply_markup=ReplyKeyboardRemove(),
    )

@main_router.message(offerNews.name)
async def set_name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(offerNews.category)
    await message.answer(
        "Выберите категорию новости: ",
        reply_markup=kb_categories
    )

@main_router.message(offerNews.category, F.text.in_(Config.CATEGORIES))
async def set_category_handler(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await state.set_state(offerNews.text)
    await message.answer(
        "Напишите текст новости: ",
        reply_markup=ReplyKeyboardRemove()
    )

@main_router.message(offerNews.category)
async def unknown_category_handler(message: Message):
    await message.reply("Такой категории не существует!")
    
@main_router.message(offerNews.text)
async def set_category_handler(message: Message, state: FSMContext):
    data = await state.update_data(text=message.text)
    await state.clear()
    await message.answer(
        "Спасибо! Ваша новость добавлена в список.",
        reply_markup=ReplyKeyboardRemove()
    )

    await post(message.bot, **data)
    print(f"{data["name"]} предложил новость в категории '{data["category"]} ':\n{data["text"]}")


@main_router.message(F.text)
async def uknown_handler(message: Message):
    await message.answer("Неизвестная команда")
