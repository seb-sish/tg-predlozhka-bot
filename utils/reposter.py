from config import Config
from aiogram import Bot

async def post(bot : Bot=None, **kwargs):
    await bot.send_message(chat_id=Config.CHAT_ID, text=format_message(**kwargs), 
                     reply_to_message_id=Config.CATEGORIES[kwargs.get('category', "")], allow_sending_without_reply=False)
    
def format_message(name='Аноним', category=None, text=None):
    return f"{name} предложил новость в категории '{category}':\n{text}"

