from datetime import date, time


from typing import Optional, List
from pydantic import BaseModel


class StatisticBase(BaseModel):
    view: int
    click: int
    cost: float


class StatisticCreate(BaseModel):
    view: int
    click: int
    cost: float


class StatisticUpdate(BaseModel):
    pass


class StatisticInDBBase(StatisticBase):
    id: Optional[int]
    date: Optional[date]
    cpc: float
    cpm: float

    class Config:
        orm_mode = True


class Statistic(StatisticInDBBase):
    pass


class Statistics(BaseModel):
    statistics: List[Statistic] = []
    amount: Optional[int]

class StatisticForTest(BaseModel):
    date: str = '2050-01-01'
    view: int
    click: int
    cost: float