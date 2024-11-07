from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage = MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(massage):
    await massage.answer('Привет! Я бот помогающий твоему здоровью.')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def fsm_handler(message,state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()
@dp.message_handler(state=UserState.growth)
async def fsm_handler(message,state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def fsm_handler(message,state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f'{data}')

#    await state.finish()

    calor = 10*float(data['weight']) + 6.25*float(data['growth']) - 5*float(data['age']) + 5


    await message.answer(f'Ваша норма калорий: {calor}')

'''
Для мужчин: (10 х вес в кг) + 
(6,25 х рост в см) – (5 х возраст в г) + 5.
'''



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)