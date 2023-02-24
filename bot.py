import os

from aiogram.types import Message
from aiogram import Bot, Dispatcher

from aiogram.utils import executor
from dotenv import load_dotenv


load_dotenv(".env")

TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def hello(message: Message):
    await message.answer("Приветствую. Я ваш помощник в мире самостоятельного изучения предметов! Я помогу вам изучить "
                         "предметы, которые вы желаете изучить. Какой предмет вы хотите изучить?")

@dp.message_handler(commands="help")
async def help(message: Message):
    await message.answer("Я помогу вам освоить необходимые вам предметы, почастям, ежедневно отправляя один параграф. "
                         "Буду присылать интересные факты по теме предмета. И задания, которые вам нужно решить, для "
                         "закрепления материала. Желательно изучать предметы по 1 за раз. Надеюсь, я вам помогу в "
                         "достижении вашей мечты, друг мой!")

@dp.message_handler(commands="objects")
async def objects(message: Message):
    await message.answer("Ваши прелметы: ")

@dp.message_handler(commands="advice")
async def advice(message: Message):
    await message.answer("У вас есть идеи как улучшить меня? Тогда напишите моему создателю @Nochi_Guardian")


if __name__ == "__main__":
    executor.start_polling(dp)
