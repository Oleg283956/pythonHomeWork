import sys
from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import logging

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage = MemoryStorage())

@dp.message_handler(text = ['00'])
async def exit_message(massage):
    print('До скорых всреч!!!')
    logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='w',
                        encoding='UTF-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    sys.exit()

@dp.message_handler(commands=['start'])
async def start_message(massage):
    await massage.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    await message.answer('Для ВЫХОДА из программы введите: "00"')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
