from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Dish(Base):
    __tablename__ = 'dishs'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=False, nullable=False)
    rest_id = Column(Integer)
    position = Column(String)
    price = Column(String)
