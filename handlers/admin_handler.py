from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import logging
from config import Config

admin_router = Router()
admin_router.message.filter(F.chat.type.in_({"supergroup"}), F.from_user.id.in_({464344058, 836206691}))

@admin_router.callback_query(F.data.startswith("change_"))
async def callbacks_num(callback: CallbackQuery):
    await callback.answer()

@admin_router.message(Command("id"))
async def id_handler(message: Message):
    await message.answer(f"Твой id: {message.from_user.id}\nid чата: {message.chat.id}\nid темы: {message.message_thread_id}")
    print(f"Твой id: {message.from_user.id} | id чата: {message.chat.id} | id темы: {message.message_thread_id}")

@admin_router.message(Command("clear"))
async def clear_handler(message: Message):
    for category in Config.CATEGORIES.keys():
        await message.bot.delete_forum_topic(Config.CHAT_ID, Config.CATEGORIES[category])
        new_topic = await message.bot.create_forum_topic(Config.CHAT_ID, category)
        Config.CATEGORIES[category] = new_topic.message_thread_id
    Config.update_categories()