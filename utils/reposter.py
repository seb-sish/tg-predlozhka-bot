from config import Config
from aiogram import Bot

async def post(bot : Bot=None, photo=None, **kwargs):
    if photo:
        await bot.send_photo(chat_id=Config.CHAT_ID, caption=format_message(**kwargs), 
        reply_to_message_id=Config.CATEGORIES[kwargs.get('category', "")], 
        photo=photo[0].file_id, allow_sending_without_reply=False)
    else:
        await bot.send_message(chat_id=Config.CHAT_ID, text=format_message(**kwargs), 
        reply_to_message_id=Config.CATEGORIES[kwargs.get('category', "")], 
        allow_sending_without_reply=False)

def format_message(name='Аноним', category=None, text=None):
    return f"{name} предложил новость в категории '{category}':\n{text}"

