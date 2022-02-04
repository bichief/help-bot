from aiogram import types

from loader import dp


@dp.inline_handler(text='')
async def empty_query(query: types.InlineQuery):
    await query.answer(results=[
        types.InlineQueryResultArticle(
            id='unknown',
            title='Пустой запрос :(',
            input_message_content=types.InputTextMessageContent(
                message_text='Я случайно сюда нажал, извините.'
            )
        )
    ])


@dp.inline_handler(text='send link')
async def goto_bot(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id='0',
                title='Поделиться ссылкой',
                description='чтобы добавить оператора, нажмите на эту кнопку :)',
                input_message_content=types.InputTextMessageContent(
                    message_text='Ваша ссылка для подключения к операторам:\n\n'
                                 't.me/tin_sup_bot?start=FSRTJ923JOSSmjfd54')
            )
        ]
    )