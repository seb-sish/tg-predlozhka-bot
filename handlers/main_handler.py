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
    await message.answer(f"Если у вас есть новость, то вы можете написать ее в этом боте. Мы все посмотрим, и если будет интересно, то расскажем в выпуске", 
                         reply_markup=kb_start)

@main_router.message(F.text == "Предложить новость")
async def offerNews_handler(message: Message, state: FSMContext):
    await state.set_state(offerNews.name)
    await message.answer(
        "Как вас зовут? Нам правда интересно)",
        reply_markup=ReplyKeyboardRemove(),
    )

@main_router.message(offerNews.name)
async def set_name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(offerNews.category)
    await message.answer(
        "По какой теме у вас новость?",
        reply_markup=kb_categories
    )

@main_router.message(offerNews.category, F.text.in_(Config.CATEGORIES))
async def set_category_handler(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await state.set_state(offerNews.text)
    await message.answer(
        "А что случилось(если вкратце)? Можете прикрепить фотокарточку, если это поможет лучше описать ситуацию",
        reply_markup=ReplyKeyboardRemove()
    )

@main_router.message(offerNews.category)
async def unknown_category_handler(message: Message):
    await message.reply("Такой категории не существует!")
    
@main_router.message(offerNews.text)
async def set_category_handler(message: Message, state: FSMContext):
    data = await state.update_data(text=message.text if message.text is not None else message.html_text)
    await state.clear()
    await message.answer(
        "Спасибо! Мы обязательно ознакомимся!",
        reply_markup=ReplyKeyboardRemove()
    )
    await post(message.bot, photo=message.photo, **data)

    print(f"{data["name"]} предложил новость в категории '{data["category"]} ':\n{data["text"]}")


@main_router.message(F.text)
async def uknown_handler(message: Message):
    await message.answer("Неизвестная команда")
