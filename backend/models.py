from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Game(Base):
    __tablename__ = "games"

    appid = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    developer = Column(String, index=True)
    publisher = Column(String, index=True)
    score_rank = Column(Float, index=True)
    positive = Column(Integer, index=True)
    negative = Column(Integer, index=True)
    userscore = Column(Float, index=True)
    owners = Column(String)
    average_forever = Column(Integer)
    average_2weeks = Column(Integer)
    median_forever = Column(Integer)
    median_2weeks = Column(Integer)
    price = Column(Integer, index=True)
    initialprice = Column(Integer)
    discount = Column(Integer)
    ccu = Column(Integer, index=True)