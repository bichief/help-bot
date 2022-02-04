from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from data import config
from keyboards.default.admin import admin_keyboard
from keyboards.inline.helper_keyboard import helper
from loader import dp


@dp.message_handler(Command('login'), user_id=config.ADMINS)
async def admin_cmd(message: types.Message):
    await message.answer('Добро пожаловать в меню администратора.\n'
                         'Выберите необходимый функционал.', reply_markup=admin_keyboard)

@dp.message_handler(Text(equals='Добавить оператора'))
async def add_helper(message: types.Message):
    await message.answer('Чтобы добавить оператора,\n'
                         'Вам необходимо нажать на кнопку ниже и следовать инструкциям.', reply_markup=helper)