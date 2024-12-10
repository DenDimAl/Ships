import datetime

from pydantic import BaseModel, Field, ConfigDict

class PortSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    town: str
    month_spendings: int