import datetime

from pydantic import BaseModel, Field, ConfigDict

class CraneSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    port_number: int
    experience: int
    month_spendings: int
