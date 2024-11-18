from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import key

api = key.api
bot = Bot(token=api)
dp = Dispatcher (bot, storage=MemoryStorage())



@dp.message_handler(text = ['Рита','Женя','son'])
async def all_message(message):
    print(f" Family {message['text']}")

@dp.message_handler(commands = ['start'])
async def start(message):
    print(f"Привет! Я бот помогающий твоему здоровью")

@dp.message_handler()
async def all_message(message):
    print(f"Введите команду /start, чтобы начать общение")





if __name__ =='__main__':
    executor.start_polling(dp,skip_updates=True)
