import datetime

from pydantic import BaseModel, Field, ConfigDict

class ScheduleOfGateSchema(BaseModel):
    NumberOfSchedule: int
    NumberOfServedCruise: int
    NumberOfGate: int
    NumberOfPort: int
    NumberOfBrigade: int
    AwaitedDateOfStart: datetime.date
    AwaitedDateOfEnd: datetime.date
    ActualDateOfStart: datetime.date
    actual_date_of_end: datetime.date