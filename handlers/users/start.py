from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp
from states.CreateRequest import CreateRequest
from utils.db_api.commands.customer import add_customer


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    deep_link = message.get_args()

    if deep_link == '':

        link_is_none = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text='Перезайти', url=f't.me/tin_sup_bot?start={message.from_user.id}')
            ]
        ])

        await message.answer('Вы нажали на /start, не указав индетификатор.\n'
                             'Если это произошло ошибочно, нажмите на кнопку ниже.', reply_markup=link_is_none)
    else:
        await message.answer(f'Здравствуйте, {message.from_user.first_name}.\n\n'
                             f'Опишите вашу проблему (фото приветствуются)\n'
                             f'И наши консультанты вам обязательно помогут.')
        await CreateRequest.first()


@dp.message_handler(state=CreateRequest.GetMessage, content_types=[types.ContentType.TEXT, types.ContentType.PHOTO])
async def create_request(message: types.Message, state: FSMContext):
    workers = 0
    if message.photo:
        file_id = message.photo[-1].file_id
        caption = message.caption
        await add_customer(telegram_id=message.from_user.id, text=caption, file_id=file_id)
        await message.answer_photo(photo=file_id, caption=f'Отлично! Я принял вашу заявку.\n'
                                                          f'<b>Ваше обращение:</b>\n\n'
                                                          f'<i>{caption}</i>\n\n'
                                                          f'Свободных операторов - {workers}\n'
                                                          f'Ожидайте ответа.')
        await state.reset_state()
    elif message.text:
        text = message.text
        await add_customer(telegram_id=message.from_user.id, text=text)
        await message.answer(f'Отлично! Я принял вашу заявку.\n'
                             f'<b>Ваше обращение:</b>\n\n'
                             f'<i>{text}</i>\n\n'
                             f'Свободных операторов - {workers}\n'
                             f'Ожидайте ответа.')
        await state.reset_state()
