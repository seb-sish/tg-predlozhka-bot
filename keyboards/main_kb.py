from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import Config

offerBtn = KeyboardButton(text="Предложить новость")
kb_start = ReplyKeyboardMarkup(keyboard=[[offerBtn]], resize_keyboard=True, one_time_keyboard=True)

categories_builder = ReplyKeyboardBuilder()
for category in Config.CATEGORIES.keys():
    categories_builder.add(KeyboardButton(text=category))
categories_builder.adjust(2, 2, 2, 2, 1)
kb_categories = categories_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)