from sqlalchemy import update, select
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.helpers import Helpers


async def add_user(telegram_id):
    try:
        async with async_sessionmaker() as session:
            await session.merge(Helpers(telegram_id=telegram_id))
            await session.commit()
    except IntegrityError:
        return True

async def update_state(telegram_id):
    async with async_sessionmaker() as session:
        common = 'true'
        state = (
            update(Helpers).where(Helpers.telegram_id == telegram_id).values(state=common)
        )

        await session.execute(state)
        await session.commit()

async def get_info(telegram_id):
    async with async_sessionmaker() as session:
        check = select(Helpers.state).where(Helpers.telegram_id == telegram_id)

        result = await session.execute(check)

        for row in result.scalars():
            return row
