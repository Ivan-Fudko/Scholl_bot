from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.inline.choice_but_start_test import towers

token = '5569348523:AAE_XIm2CJIiC_2YMSJI09HYJV4yuTnG2Is'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
b = towers()
