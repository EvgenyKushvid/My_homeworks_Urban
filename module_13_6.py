from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import key
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

api = key.api
bot = Bot(token=api)
dp = Dispatcher (bot, storage=MemoryStorage())

# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# button1 = KeyboardButton(text='О боте')
# button2 = KeyboardButton(text='Расчитать Ккал')
# kb.add(button1,button2)

kb_in = InlineKeyboardMarkup(resize_keyboard=True)
btn1 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
btn2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
kb_in.add(btn1,btn2)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await  call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await  call.answer()


@dp.message_handler(commands = ['start'])
async def  start (message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Для всего интересного введи "Расчитать"')

@dp.message_handler(text = 'Расчитать')
async def  main_menu (message):
    await message.answer(' Выберите опцию:',reply_markup = kb_in )





class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()

@dp.callback_query_handler(text = 'calories')
async def set_age (call):
    await call.message.answer('Расчитаем количество ККАЛ для тебя..)), если ты мужчина конечно.. для девочек пока что не умею. Ответь на несколько вопросов...)')
    await call.message.answer('Сколько тебе лет?')
    await UserState.age.set()


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Какой у тебя рост?')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Ну и нескромный вопрос.. вес какой?')
    await UserState.weight.set()


@dp.message_handler(state = UserState.weight)
async def send_calories(message,state):
    await state.update_data( weight = message.text)
    data  = await state.get_data()
    #для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
    # 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161
    #доделать блок с мальчиком или девочкой. понять как выбирать из вариантов
    calories = (10*int(data['weight'])) + (6.25 * int(data['growth'])) - (5*int(data['age'])) + 5
    await message.answer(f"По мнению Миффлина-Сан Жеора для оптимального похудения или сохранения нормального веса тебе нужно {calories} Ккал )))")
    await state.finish()


@dp.message_handler(text = ['Рита', 'рита','Марго','Маргарита', 'маргарита', 'марго'])
async def all_message(message):
    print(f" Family {message['text']}")
    await message.answer("Рита + Женя  = Любовь! ;)")


@dp.message_handler()
async def all_message(message):
    await message.answer(f"Введите команду /start, чтобы начать общение")






if __name__ =='__main__':
    executor.start_polling(dp,skip_updates=True)
