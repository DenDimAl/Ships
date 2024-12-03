import datetime

from pydantic import BaseModel, Field, ConfigDict

class ClientSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    FaceNumber: int
    NameOfTheFirm: str
    AccompalienceDate: datetime.date | None = Field(default=None)
    StateOrPrivate: bool