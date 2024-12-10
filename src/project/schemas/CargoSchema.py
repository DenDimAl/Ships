import datetime

from pydantic import BaseModel, Field, ConfigDict

class CargoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    cargo_type: str
    volume: int
    containments: str
    weight: int
    delivery_cost: int | None = Field(default=None)