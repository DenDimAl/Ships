import datetime

from pydantic import BaseModel, Field, ConfigDict

class LoaderSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    personnel_number: str
    fio: str
    responsobility: str
    experience: int
    paycheck: int