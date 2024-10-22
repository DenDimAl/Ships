from pydantic import BaseModel, Field, ConfigDict

class ShipSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    NumberOfShip: int
    Name: str | None = Field(default=None)
    ShipType: str
    MaxVolume: int
    MaxWeight: int
    Speed: int
    Spendings: int
    FuelSpendings: int
#То есть мне тут просто продолжать перечислять таблички?