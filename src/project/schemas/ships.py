import datetime

from pydantic import BaseModel, Field, ConfigDict

class ShipCreateUpdateSchema(BaseModel):
    Name: str | None = Field(default=None)
    ShipType: str
    MaxVolume: int
    MaxWeight: int
    Speed: int
    Spendings: int
    FuelSpendings: int

class ShipSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    NumberOfShip: int

"""
class CargoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    NumberOfCargo : int
    CargoType: str
    Volume: int
    Containments: str
    Weight: int
    DeliveryCost: str | None = Field(default=None)

class ClientSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    FaceNumber: int
    NameOfTheFirm: str
    AccompalienceDate: datetime.date | None = Field(default=None)
    StateOrPrivate: bool

class SupplierSchema(BaseModel):
    FaceNumber: int
    NameOfTheFirm: str
    AccompalienceDate: datetime.date | None = Field(default=None)
    StateOrPrivate: bool

class CaptainSchema(BaseModel):
    PersonnelNumber: str
    FIO: str
    Experience: int
    PayCheck: int

class LoaderSchema(BaseModel):
    PersonnelNumber: str
    FIO: str
    Experience: int
    PayCheck: int

class CraneSchema(BaseModel):
    NumberOfCrane: int
    PortNumber: int
    Experience: int
    MonthSpendings: int

class PortSchema(BaseModel):
    NumberOfPort: int
    Town: str
    MonthSpendings: int

class GateSchema(BaseModel):
    NumberOfGate: int
    NumberInPort: int
    NumberOfPort: int
    NumberOfCrane: int

class RouteSchema(BaseModel):
    NumberOfRoute: int
    NumberOfStartingPoint: int
    NumberOfEndingPoint: int
    RouteLengrh: int

class CruiseSchema(BaseModel):
    NumberOfCruise: int
    AwaitingDateOfStart: datetime.date
    AwaitingDateOfEnd: datetime.date
    ActualDateOfStart: datetime.date | None = Field(default=None)
    ActualDateOfEnd: datetime.date | None = Field(default=None)
    Ship: int
    Captain: str
    TypeOfCargo: str
    NumberOfRoute: int

class BrigadeSchema(BaseModel):
    Id: int
    NumberOfBrigade: int
    SignedEmployee: str

class ScheduleOfGateSchema(BaseModel):
    NumberOfSchedule: int
    NumberOfServedCruise: int
    NumberOfGate: int
    NumberOfPort: int
    NumberOfBrigade: int
    AwaitedDateOfStart: datetime.date
    AwaitedDateOfEnd: datetime.date
    ActualDateOfStart: datetime.date
    ActualDateOfEnd: datetime.date

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
"""