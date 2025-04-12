import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from aiogram import Bot, Dispatcher
from services.setting_up_commands import set_default_commands
from services.logger import logger
from handlers.important_handlers import important_route

bot = Bot(config("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

async def main():
    logger.info("func 'Main' has been running")
    dp.include_router(important_route)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_default_commands(logger, bot, True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run((main()))