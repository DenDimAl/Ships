import datetime

from pydantic import BaseModel, Field, ConfigDict

class CaptainSchema(BaseModel):
    PersonnelNumber: str
    Fio: str
    Experience: int
    Paycheck: int