import datetime

from pydantic import BaseModel, Field, ConfigDict

class OrderSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number_of_order: int
    number_of_cargo: int
    number_of_client: int
    number_of_supplier: int
    date_of_ordering: datetime.date
    awaiting_date_of_receiving: datetime.date
    actual_date_of_receiving: datetime.date | None = Field(default=None)
    awaiting_date_of_deliviring: datetime.date | None = Field(default=None)
    actual_date_of_deliviring: datetime.date | None = Field(default=None)
    number_of_cruise: int
    cost_of_delivery: int