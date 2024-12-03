import datetime

from pydantic import BaseModel, Field, ConfigDict

class BrigadeSchema(BaseModel):
    Id: int
    NumberOfBrigade: int
    SignedEmployee: str