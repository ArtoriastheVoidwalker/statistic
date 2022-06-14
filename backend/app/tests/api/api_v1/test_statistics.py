import random
from typing import Dict
from datetime import datetime as datatime, timedelta

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from datetime import datetime as dt
from app.models import Statistic

from app import crud, schemas
from app.core.config import settings
from app.schemas.statistic import StatisticCreate, StatisticForTest


def test_create_statistic_200(
    client: TestClient, db: Session,
) -> None:

    statistic_data = schemas.StatisticCreate(
        date=dt.now(),
        view=random.randint(0, 1000),
        click=random.randint(0, 1000),
        cost=round(random.uniform(0, 10),2),
        cpc=round(random.randint(0, 1000)/random.randint(0, 1000), 2),# Значение cpc округляется до копейки            
        cpm=round((random.randint(0, 1000)/random.randint(0, 1000))*1000, 2),# Значение cpm округляется до копейки
    )

    request = client.post(
        f"{settings.API_V1_STR}/statistics/",
        # headers=superuser_token_headers,
        json=statistic_data.dict()
    )

    # next_statistic_data = schemas.StatisticForTest(
    #     date='2050-01-01',
    #     view=random.randint(0, 1000),
    #     click=random.randint(0, 1000),
    #     cost=round(random.uniform(0, 10),2),
    #     cpc=round(random.randint(0, 1000)/random.randint(0, 1000), 2),# Значение cpc округляется до копейки            
    #     cpm=round((random.randint(0, 1000)/random.randint(0, 1000))*1000, 2),# Значение cpm округляется до копейки
    # )
    # next_request = client.post(
    #     f"{settings.API_V1_STR}/statistics/",
    #     json=next_statistic_data.dict()
    # )
    # breakpoint()

    assert 200 == request.status_code #next_request.status_code


# def test_create_statistic_401_view(
#     client: TestClient, db: Session,
# ) -> None:

#     statistic_data = schemas.StatisticCreate(
#         date=dt.now(),
#         view='error',
#         click=random.randint(0, 1000),
#         cost=round(random.uniform(0, 10),2),
#         cpc=round(random.randint(0, 1000)/random.randint(0, 1000), 2),# Значение cpc округляется до копейки            
#         cpm=round((random.randint(0, 1000)/random.randint(0, 1000))*1000, 2),# Значение cpm округляется до копейки
#     )

#     request = client.post(
#         f"{settings.API_V1_STR}/statistics/",
#         json=statistic_data.dict()
#     )
#     assert 401 == request.status_code


# def test_create_statistic_401_click(
#     client: TestClient, db: Session,
# ) -> None:

#     statistic_data = schemas.StatisticCreate(
#         date=dt.now(),
#         view=random.randint(0, 1000),
#         click='error',
#         cost=round(random.uniform(0, 10),2),
#         cpc=round(random.randint(0, 1000)/random.randint(0, 1000), 2),# Значение cpc округляется до копейки            
#         cpm=round((random.randint(0, 1000)/random.randint(0, 1000))*1000, 2),# Значение cpm округляется до копейки
#     )

#     request = client.post(
#         f"{settings.API_V1_STR}/statistics/",
#         json=statistic_data.dict()
#     )
#     assert 401 == request.status_code


# def test_create_statistic_401_date(
#     client: TestClient, db: Session,
# ) -> None:

#     statistic_data = schemas.StatisticCreate(
#         date='error',
#         view=random.randint(0, 1000),
#         click=random.randint(0, 1000),
#         cost=round(random.uniform(0, 10),2),
#         cpc=round(random.randint(0, 1000)/random.randint(0, 1000), 2),# Значение cpc округляется до копейки            
#         cpm=round((random.randint(0, 1000)/random.randint(0, 1000))*1000, 2),# Значение cpm округляется до копейки
#     )

#     request = client.post(
#         f"{settings.API_V1_STR}/statistics/",
#         json=statistic_data.dict()
#     )
#     assert 401 == request.status_code


def test_get_statistics_404(
    client: TestClient, db: Session
) -> None:
    from_date = crud.statistic.get_first(db=db).date
    statistics = (
            db
            .query(Statistic)
            .order_by(Statistic.date)
            .all()
        )
    to_date = statistics[-1].date
    r = client.get(f"{settings.API_V1_STR}/statistic/?from_date={str(from_date)[:10]}&to_date={str(to_date)[:10]}")
    request = r.json()
    assert 404 <= r.status_code
    assert request


def test_get_statistics_400_from_date(
    client: TestClient, db: Session
) -> None:
    statistics = (
            db
            .query(Statistic)
            .order_by(Statistic.date)
            .all()
        )
    to_date = statistics[-1].date
    request = client.get(f"{settings.API_V1_STR}/statistic/?from_date=error&to_date={str(to_date)[:10]}")
    assert request.status_code == 404


def test_get_statistics_404_to_date(
    client: TestClient, db: Session
) -> None:
    from_date = crud.statistic.get_first(db=db).date
    request = client.get(f"{settings.API_V1_STR}/statistic/?from_date={str(from_date)[:10]}&to_date=error")
    assert request.status_code == 404


def test_get_statistics_404_time_interval(
    client: TestClient, db: Session
) -> None:
    from_date = '2022-07-14'
    to_date = '2022-06-14'
    request = client.get(f"{settings.API_V1_STR}/statistic/?from_date={from_date}&to_date={to_date}")
    assert request.status_code == 404


def test_delete_user(client: TestClient, db: Session) -> None:
    request = client.delete(
        f"{settings.API_V1_STR}/statistics/",
    )
    assert request
    assert 200 == request.status_code
