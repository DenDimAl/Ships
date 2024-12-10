import datetime

from pydantic import BaseModel, Field, ConfigDict

class CaptainSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    personnel_number: str
    fio: str
    experience: int
    paycheck: int