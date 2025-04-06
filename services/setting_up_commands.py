from aiogram.types import BotCommand
from run import bot

bot.set_my_commands(
    commands=[
        BotCommand("start", "начать разговор с ботом"),
        BotCommand("help", "попросить о помощи у бота"),
        BotCommand("edit", "изменить бота"),
        BotCommand("bye", "попрощаться с ботом")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)