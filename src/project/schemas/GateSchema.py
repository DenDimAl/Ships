import datetime

from pydantic import BaseModel, Field, ConfigDict

class GateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number_in_port: int
    number_of_port: int
    number_of_crane: int