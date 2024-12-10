import datetime

from pydantic import BaseModel, Field, ConfigDict

class ScheduleOfGateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number_of_schedule: int
    number_of_served_cruise: int
    number_of_gate: int
    number_of_port: int
    number_of_brigade: int
    awaited_date_of_start: datetime.date
    awaited_date_of_end: datetime.date
    actual_date_of_start: datetime.date
    actual_date_of_end: datetime.date