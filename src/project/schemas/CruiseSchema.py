import datetime

from pydantic import BaseModel, Field, ConfigDict

class CruiseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number_of_cruise: int
    awaiting_date_of_start: datetime.date
    awaiting_date_of_end: datetime.date
    actual_date_of_start: datetime.date
    actual_date_of_end: datetime.date
    ship: int
    captain: str
    type_of_cargo: str
    number_of_route: int