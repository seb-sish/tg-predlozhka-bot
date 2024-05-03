from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import Config
import asyncio
import logging
import sys

from handlers import main_router, admin_router

dp = Dispatcher(storage=MemoryStorage())


async def set_default_commands(bot):
     await bot.set_my_commands(commands=[
        BotCommand(command="start", description="Начать диалог")
        ])


def add_routers(dp):
    dp.include_router(main_router)
    dp.include_router(admin_router)


async def main() -> None:
    bot = Bot(Config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await set_default_commands(bot)

    add_routers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())