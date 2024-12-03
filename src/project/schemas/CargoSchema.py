import datetime

from pydantic import BaseModel, Field, ConfigDict

class CargoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    NumberOfCargo : int
    CargoType: str
    Volume: int
    Containments: str
    Weight: int
    DeliveryCost: str | None = Field(default=None)