import datetime

from pydantic import BaseModel, Field, ConfigDict

class OrderSchema(BaseModel):
    NumberOfOrder: int
    NumberOfCargo: int
    NumberOfClient: int
    NumberOfSupplier: int
    DateOfOrdering: datetime.date
    AwaitingDateOfReceiving: datetime.date
    ActualDateOfReceiving: datetime.date | None = Field(default=None)
    AwaitingDateOfDeliviring: datetime.date | None = Field(default=None)
    ActualDateOfDeliviring: datetime.date | None = Field(default=None)
    NumberOfCruise: int
    CostOfDelivery: int