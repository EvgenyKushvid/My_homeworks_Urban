from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import key

api = key.api
bot = Bot(token=api)
dp = Dispatcher (bot, storage=MemoryStorage())



@dp.message_handler(text = ['Рита'])
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
