import json
import os

data = {}
with open("speech/speech_ru.json", "r", encoding="UTF-8") as file:
    data = json.load(file)