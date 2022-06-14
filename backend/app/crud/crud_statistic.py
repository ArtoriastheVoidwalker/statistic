from typing import Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Statistic
from app.schemas import StatisticCreate, StatisticUpdate
from datetime import datetime as dt


class CRUDStatistic(CRUDBase[Statistic, StatisticCreate, StatisticUpdate]):  

    def get_by_date(
        self,
        db: Session, *, 
        from_date: dt, 
        to_date: dt,
        skip: int = 0,
        limit: int = 100
    ) -> Optional[Statistic]:

        statistics = (
            db
            .query(Statistic)
            .order_by(Statistic.date)
            .offset(skip)
            .limit(limit)
            .all()
        )
        result = []
        amount = 0
        for statistic in statistics:
            if from_date <= statistic.date <= to_date:
                result.append(statistic)
                amount+=1
        

        return {'statistics': result, 'amount': amount}
  

    def save(self, db: Session, *, obj_in: StatisticCreate) -> Statistic:

        db_obj = Statistic(
            date=dt.now(),
            view=obj_in.view,
            click=obj_in.click,
            cost=obj_in.cost,
            cpc=round(obj_in.cost/obj_in.click, 2),# Значение cpc округляется до копейки
            cpm=round((obj_in.cost/obj_in.view)*1000, 2),# Значение cpm округляется до копейки
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


statistic = CRUDStatistic(Statistic)
