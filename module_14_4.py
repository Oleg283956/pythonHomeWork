from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions

l_all_prod = crud_functions.get_all_products()

#--------- КЛАВЫ ------------------
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
kb.add(button1,button2)
kb.row(button3)

kbInl = InlineKeyboardMarkup(resize_keyboard=True)
butt1Inl = InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')
butt2Inl = InlineKeyboardButton(text='Формулы расчёта',callback_data='formulas')
kbInl.add(butt1Inl,butt2Inl)

kbInl1 = InlineKeyboardMarkup(resize_keyboard=True)
butt1Inl1 = InlineKeyboardButton(text='Product1',callback_data='product_buying')
butt1Inl2 = InlineKeyboardButton(text='Product2',callback_data='product_buying')
butt1Inl3 = InlineKeyboardButton(text='Product3',callback_data='product_buying')
butt1Inl4 = InlineKeyboardButton(text='Product4',callback_data='product_buying')
kbInl1.add(butt1Inl1,butt1Inl2,butt1Inl3,butt1Inl4)

#--------- END КЛАВЫ ------------------


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage = MemoryStorage())



@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(commands=['start'])
async def starter(massage):
    await massage.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup = kb)


@dp.message_handler(text = 'Рассчитать')
async def rasschitat(message):
    await message.answer('Выбери опцию:',reply_markup = kbInl)


@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    for i in range(0,len(l_all_prod)):
        with open(f'files/{i+1}.png','rb') as img:
            await message.answer_photo(img,f'Название: {l_all_prod[i][1]}. Описание: {l_all_prod[i][2]} Цена: {l_all_prod[i][3]}. ')
    await message.answer('Выберите продукт для покупки:',reply_markup = kbInl1)




class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


#--------- ФОРМУЛА -------------
@dp.callback_query_handler(text = 'formulas')
async def rasshnorm(call):
    await call.message.answer('10xвес(кг)+6,25xрост(см)-5xвозраст(г)-161')
    await call.answer()
#--------- END ФОРМУЛА -------------



#--------- Рассчёт калорий ------------------

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

    await state.finish()

    calor = 10*float(data['weight']) + 6.25*float(data['growth']) - 5*float(data['age']) - 161

    await message.answer(f'Ваша норма калорий: {calor}',reply_markup = kb)

#--------- END Рассчёт калорий ------------------





if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
