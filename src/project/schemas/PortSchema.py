import datetime

from pydantic import BaseModel, Field, ConfigDict

class PortSchema(BaseModel):
    NumberOfPort: int
    Town: str
    MonthSpendings: int