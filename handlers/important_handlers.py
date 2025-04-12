from random import choice
from symbol import lambdef

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from services.logger import logger
from speech.speech import data
from keyboards.keyboards import choice_of_item_keyboard, choice_to_play_the_game_keyboard


important_route = Router()

is_play = False

@important_route.message(CommandStart())
async def start_process(message: Message):
    await message.answer(data["/start"], reply_markup=choice_to_play_the_game_keyboard() if not is_play else None)

@important_route.message(Command("help"))
async def start_process(message: Message):
    await message.answer(data["/help"], reply_markup=choice_to_play_the_game_keyboard() if not is_play else None)

@important_route.message(lambda msg: msg.text == data["inline_keyboards"]["choice_to_play_the_game_kb"][0])
async def play_the_game_process(message: Message):
    global is_play
    is_play = True
    await message.answer(data["play_the_game"], reply_markup=choice_of_item_keyboard())

@important_route.message(F.text.in_(data["inline_keyboards"]["choice_of_item_kb"]))
async def message_total_of_the_game(message: Message):
    if not is_play:
        return
    items = data["inline_keyboards"]["choice_of_item_kb"]
    item = choice(items)
    logger.info("The bot has chosen the " + item)
    winner = ""
    if item == message.text:
        winner = data["winners"][0]
    else:

        if item == items[0]: # Камень
            if message.text == items[1]: #Ножницы
                winner = data["winners"][1]
            else: # Бумага
                winner = data["winners"][2]
        elif item == items[1]: # Ножницы
            if message.text == items[2]: # Бумага
                winner = data["winners"][1]
            else:  # Камень
                winner = data["winners"][2]
        elif item == items[2]: # Бумага
            if message.text == items[0]: # Камень
                winner = data["winners"][1]
            else: # Ножницы
                winner = data["winners"][2]

    await message.answer(data["total_of_the_game"][0] + winner)
    await message.answer(data["total_of_the_game"][1], reply_markup=choice_to_play_the_game_keyboard())

@important_route.message(lambda msg: msg.text == data["inline_keyboards"]["choice_to_play_the_game_kb"][1])
async def not_play_the_game_process(message: Message):
    await message.answer(data["not_play_the_game"], reply_markup=choice_to_play_the_game_keyboard())

@important_route.message()
async def reply_to_any_unexcepted_message_process(message: Message):
    await message.reply(data["any_unexpected_commands"])