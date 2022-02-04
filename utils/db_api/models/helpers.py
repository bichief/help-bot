
from sqlalchemy import Column, Integer, BigInteger, String, sql

from utils.db_api.base import Base


class Helpers(Base):
    __tablename__ = 'helpers'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger(), unique=True, nullable=False)
    state = Column(String(), default='false')

    query: sql.Select
