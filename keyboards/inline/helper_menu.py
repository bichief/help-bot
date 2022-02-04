from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.commands.customer import get_information

menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Перейти в меню', callback_data='menu')
    ]
])

helper_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=
[
    [
        InlineKeyboardButton(text='Выйти на смену', callback_data='start_work')
    ],
    [
        InlineKeyboardButton(text='Вопросы', callback_data='questions')
    ]
])


async def get_customers():
    customers = InlineKeyboardMarkup(row_width=1)

    array = await get_information()

    for row in array:
        btn = InlineKeyboardButton(text=f'{row}', callback_data=f'customer_{row}')
        customers.add(btn)
    return customers
