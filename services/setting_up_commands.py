from aiogram.types import BotCommand

async def set_default_commands(logger, bot, set = False):
    if not set:
        return
    logger.info("Computer is uploading the commands")
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="начать диалог с ботом"),
            BotCommand(command="help", description="помощь с ботом"),
            BotCommand(command="/start_game", description="начать игру")
        ],
        # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
        # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
    )