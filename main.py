from decouple import config

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from parse_price import get_ozon_product_prices

BOT_TOKEN = config('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Этот бот выдает цену на товар в "Ozon" по его ссылке. Желаю удачи!')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Этот бот очень прост, вставьте вашу ссылку на товар в "Ozon" и он выдаст Вам ее цену.')


@dp.message()
async def get_price(message: Message):
    await message.answer(text='Это займет около 10 секунд.')
    prices = get_ozon_product_prices(message.text)
    await message.reply(text=prices)


if __name__ == '__main__':
    dp.run_polling(bot)
