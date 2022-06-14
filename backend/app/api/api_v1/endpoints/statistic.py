from typing import Any
from datetime import datetime as datatime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps


router = APIRouter()

@router.get("/", response_model=schemas.Statistics)
async def get_by_date(
    from_date: str, 
    to_date: str,
    page: int = 1,
    count: int = 10,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        valid_from_date = datatime.strptime(from_date, '%Y-%m-%d')
        valid_to_date = datatime.strptime(to_date, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=400, detail='Type error: valid_from_date or valid_to_date')
    if valid_from_date > valid_to_date:
        raise HTTPException(status_code=400, detail='Time interval set incorrectly')

    skip = (page - 1) * count
    statistics = crud.statistic.get_by_date(
        db,
        from_date=valid_from_date, 
        to_date=valid_to_date + timedelta(days=1),# Добавим один день,чтобы включить окончание периода(
                                                  # т.к. время,по умолчанию,00:00:00 => cтатистика этого дня не войдёт в диапазон,
                                                  # если не добавить сутки.)
        skip=skip,
        limit=count
    )

    return statistics


@router.post("/", response_model=schemas.Statistic)
async def save(
    *,
    db: Session = Depends(deps.get_db),
    statistic_data: schemas.StatisticCreate,
) -> Any:

    return crud.statistic.save(db, obj_in=statistic_data)


@router.delete("/")
async def delete(
    db: Session = Depends(deps.get_db),
):
    list_statistic = crud.statistic.get_multi(db)
    for statistic in range(len(list_statistic)):
        crud.statistic.remove(db, id=list_statistic[statistic].id)
