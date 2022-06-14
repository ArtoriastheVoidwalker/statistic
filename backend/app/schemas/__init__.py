from pydantic import BaseModel
from typing import Optional

from .statistic import Statistic, StatisticCreate, Statistics, StatisticUpdate, StatisticForTest
# from .user import (
#     User, Users, UserCreate, UserUpdate,
#     UserLogin, ValidateCode
# )

class DefaultResponseSchema(BaseModel):

    status_code: Optional[int] = 200
    success: Optional[bool] = True
