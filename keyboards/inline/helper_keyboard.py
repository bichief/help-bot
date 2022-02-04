from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

helper = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Отправить ссылку.', switch_inline_query='send link')
    ]
])