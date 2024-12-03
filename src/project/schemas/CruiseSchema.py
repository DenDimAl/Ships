import datetime

from pydantic import BaseModel, Field, ConfigDict

class CruiseSchema(BaseModel):
    NumberOfCruise: int
    AwaitingDateOfStart: datetime.date
    AwaitingDateOfEnd: datetime.date
    ActualDateOfStart: datetime.date | None = Field(default=None)
    ActualDateOfEnd: datetime.date | None = Field(default=None)
    Ship: int
    Captain: str
    TypeOfCargo: str
    NumberOfRoute: int