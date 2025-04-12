from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from speech.speech import data

def choice_to_play_the_game_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=name) for name in data["inline_keyboards"]["choice_to_play_the_game_kb"]]],
        one_time_keyboard=True)

def choice_of_item_keyboard():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=name) for name in data["inline_keyboards"]["choice_of_item_kb"]]], one_time_keyboard=True)