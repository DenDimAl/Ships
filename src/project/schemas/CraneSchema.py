import datetime

from pydantic import BaseModel, Field, ConfigDict

class CraneSchema(BaseModel):
    NumberOfCrane: int
    PortNumber: int
    Experience: int
    MonthSpendings: int
