from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import key
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


api = key.api
bot = Bot(token=api)
dp = Dispatcher (bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()


@dp.message_handler(text = 'Calories')
async def set_age (message):
    await message.answer('Сколько тебе лет?')
    await UserState.age.set()


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес')
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


@dp.message_handler(text = 'Рита')
async def all_message(message):
    print(f" Family {message['text']}")
    await message.answer("Рита + Женя  = Любовь! ;)")

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer(f"Привет! Я бот помогающий твоему здоровью")
    await message.answer("Рад видеть тебя в моем боте")

@dp.message_handler()
async def all_message(message):
    await message.answer(f"Введите команду /start, чтобы начать общение")
    #await message.answer(f'Это пока что не поняно что такое {message.text.upper()}')





if __name__ =='__main__':
    executor.start_polling(dp,skip_updates=True)
