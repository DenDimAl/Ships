import datetime

from pydantic import BaseModel, Field, ConfigDict

class SupplierSchema(BaseModel):
    FaceNumber: int
    NameOfTheFirm: str
    AccompalienceDate: datetime.date | None = Field(default=None)
    StateOrPrivate: bool