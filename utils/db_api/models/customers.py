from sqlalchemy import Column, Integer, BigInteger, String, sql

from utils.db_api.base import Base


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger(), unique=True, nullable=False)
    text = Column(String(255), nullable=False)
    file_id = Column(String())
    state = Column(String(), default='false')

    query: sql.Select