from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateRequest(StatesGroup):
    GetMessage = State()