from pydantic import BaseModel
from typing import Optional, List

class GameOut(BaseModel):
    appid: int
    name: str
    developer: str
    publisher: str
    score_rank:float
    positive: int
    negative: int
    userscore: float
    owners: str
    average_forever: int
    average_2weeks: int
    median_forever: int
    median_2weeks: int
    price: int
    initialprice: int
    discount: int
    ccu: int

    class Config:
        orm_mode = True

class GameSearchResults(BaseModel):
    results: List[GameOut]
    total: int