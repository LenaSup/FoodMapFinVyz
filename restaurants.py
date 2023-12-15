from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Rest(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String)
    coords_x = Column(Integer)
    coords_y = Column(Integer)