from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.sql.sqltypes import Float
from app.db.base_class import Base
from datetime import datetime as dt


class Statistic(Base):

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False, default=dt.now)
    view = Column(Integer, nullable=False)
    click = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    cpc = Column(Float, nullable=False)
    cpm = Column(Float, nullable=False)


