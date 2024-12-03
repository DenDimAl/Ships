import datetime

from pydantic import BaseModel, Field, ConfigDict

class LoaderSchema(BaseModel):
    PersonnelNumber: str
    FIO: str
    Experience: int
    PayCheck: int