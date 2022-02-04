from aiogram import types

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer('Я вас не понял.\n'
                         'Воспользуйтесь командой /start')


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message):
    await message.answer('Я вас не понял. Отправьте ваше обращение еще раз.\n\n'
                         'Я принимаю - текст, фото')

