from multiprocessing import *
from time import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from aiogram import Bot
from config import Config

async def start_process(bot : Bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(clear_topics, 'cron', kwargs={"bot":bot}, day_of_week="mon", hour="0")
    scheduler.start()


async def clear_topics(bot):
    for category in Config.CATEGORIES.keys():
        await bot.delete_forum_topic(Config.CHAT_ID, Config.CATEGORIES[category])
        new_topic = await bot.create_forum_topic(Config.CHAT_ID, category)
        Config.CATEGORIES[category] = new_topic.message_thread_id
    Config.update_categories()