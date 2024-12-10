import datetime

from pydantic import BaseModel, Field, ConfigDict

class ClientSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    face_number: int
    name_of_the_firm: str
    accompalience_date: datetime.date | None = Field(default=None)
    state_or_private: bool