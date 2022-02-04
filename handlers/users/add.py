import time

from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Text

from keyboards.inline.helper_menu import helper_menu, menu, get_customers
from loader import dp
from utils.db_api.commands.helper import add_user, update_state, get_info


@dp.message_handler(CommandStart(deep_link='FSRTJ923JOSSmjfd54'))
async def start_add_cmd(message: types.Message):
    await add_user(telegram_id=message.from_user.id)
    await message.answer('Здравствуйте. Вы были успешно занесены в таблицу операторов.\n\n'
                         'Ваше меню доступно по кнопке ниже.', reply_markup=menu)


@dp.callback_query_handler(Text(equals='menu'))
async def menu_callback(call: types.CallbackQuery):
    await call.message.answer('Вы находитесь в меню.', reply_markup=helper_menu)

@dp.callback_query_handler(Text(equals='start_work'))
async def start_work(call: types.CallbackQuery):
    await update_state(telegram_id=call.from_user.id)
    await call.message.answer('Вы успешно начали свою работу!')

@dp.callback_query_handler(Text(equals='questions'))
async def questions_work(call: types.CallbackQuery):
    state = await get_info(telegram_id=call.from_user.id)
    if state != 'true':
        await call.message.answer('Сперва нажмите на кнопку\n'
                                  '<b>Выйти на смену!</b>')
    else:
        keyboard = await get_customers()
        await call.message.answer('Перед вами находятся необработанные клиенты.', reply_markup=keyboard)
