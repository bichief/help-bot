from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.customers import Customers


async def add_customer(telegram_id, text, file_id=None):
    try:
        async with async_sessionmaker() as session:
            await session.merge(Customers(telegram_id=telegram_id, text=text, file_id=file_id))
            await session.commit()
    except IntegrityError:
        return True

async def get_information():
    array = []
    async with async_sessionmaker() as session:
        check = select(Customers.telegram_id).where(Customers.state == 'false')

        result = await session.execute(check)

        for row in result.scalars():
            if row not in array:
                array.append(row)
        return array


