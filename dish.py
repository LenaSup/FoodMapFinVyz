from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Dish(Base):
    __tablename__ = 'dishs'
    rest_id = Column(Integer, primary_key=True, unique=True, autoincrement=False, nullable=False)
    position = Column(String)
    price = Column(String)
