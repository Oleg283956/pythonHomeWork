from gettext import textdomain

from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
kb.add(button1,button2)



kbInl = InlineKeyboardMarkup(resize_keyboard=True)
butt1Inl = InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')
butt2Inl = InlineKeyboardButton(text='Формулы расчёта',callback_data='formulas')
kbInl.add(butt1Inl,butt2Inl)



api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage = MemoryStorage())


@dp.message_handler(commands=['start'])
async def starter(massage):
    await massage.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')
async def rasschitat(message):
    await message.answer('Выбери опцию:',reply_markup = kbInl)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.callback_query_handler(text = 'formulas')
async def rasshnorm(call):
    await call.message.answer('10 x вес(кг)+6,25 x рост(см)-5 x возраст(г)-161')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def rasshnorm(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()

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
#    await message.answer(f'{data}')

    await state.finish()

    calor = 10*float(data['weight']) + 6.25*float(data['growth']) - 5*float(data['age']) - 161


    await message.answer(f'Ваша норма калорий: {calor}')




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
