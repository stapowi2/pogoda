from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from main import *
import json

bot = Bot(token='7189801995:AAGSQmcGr4cP9KUMZWh66hNWsUkHBoY2gg0')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
   start_button = ['Дюртюли', 'Уфа', 'Екатеринбург', 'Москва', 'Казань', 'Санкт-Петербург']
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   keyboard.add(*start_button)

   await message.answer('Нажмите на кнопку', reply_markup=keyboard)

@dp.message_handler(Text(equals='Дюртюли'))
async def get_pogoda_dyurtyuli(message: types.Message):
   dyurtyuli()

   with open('pog.json') as file:
      data = json.load(file)

      await message.answer(data)

@dp.message_handler(Text(equals='Уфа'))
async def get_pogoda_ufa(message: types.Message):
   ufa()

   with open('pog.json') as file:
      data = json.load(file)

      await message.answer(data)

@dp.message_handler(Text(equals='Екатеринбург'))
async def get_pogoda_yekaterinburg(message: types.Message):
   yekaterinburg()

   with open('pog.json') as file:
      data = json.load(file)

      await message.answer(data)

@dp.message_handler(Text(equals='Москва'))
async def get_pogoda_moscow(message: types.Message):
   moscow()

   with open('pog.json') as file:
      data = json.load(file)

      await message.answer(data)

@dp.message_handler(Text(equals='Казань'))
async def get_pogoda_kazan(message: types.Message):
   kazan()

   with open('pog.json') as file:
      data = json.load(file)

      await message.answer(data)

@dp.message_handler(Text(equals='Санкт-Петербург'))
async def get_pogoda_saint_peterburg(message: types.Message):
   saint_peterburg()

   with open('pog.json') as file:
      data = json.load(file)

      await message.answer(data)



def main():
   executor.start_polling(dp)

if __name__ == '__main__':
   main()
