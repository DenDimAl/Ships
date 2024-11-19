from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, ForeignKey

from src.project.infrastructure.postgres.database import Base

class Ship(Base):
    __tablename__ = "ships"

    NumberOfShip: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(nullable=True)
    ShipType: Mapped[str] = mapped_column(nullable=False)
    Speed: Mapped[int] = mapped_column(nullable=False)
    Spendings: Mapped[int] = mapped_column(nullable=False)
    FuelSpendings: Mapped[int] = mapped_column(nullable=False)

class Suppliers(Base):
    __tablename__ = "suppliers"

    FaceNumber: Mapped[int] = mapped_column(primary_key=True)
    NameOfTheFirm: Mapped[str] = mapped_column(nullable=False)
    AccompalienceDate: Mapped[datetime] = mapped_column(nullable=True)
    StateOrPrivate: Mapped[bool] = mapped_column(default=False)

class Clients(Base):
    __tablename__ = "clients"

    FaceNumber: Mapped[int] = mapped_column(primary_key=True)
    NameOfTheFirm: Mapped[str] = mapped_column(nullable=False)
    AccompalienceDate: Mapped[datetime] = mapped_column(nullable=True)
    StateOrPrivate: Mapped[bool] = mapped_column(default=False)

class Ports(Base):
    __tablename__ = "ports"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Town: Mapped[str] = mapped_column(nullable=False)
    MonthSpendings: Mapped[int] = mapped_column(nullable=False)

class Loaders(Base):
    __tablename__ = "loaders"

    PersonnelNumber: Mapped[str] = mapped_column(primary_key=True)
    Fio: Mapped[str] = mapped_column(nullable=False)
    Responsobility: Mapped[str] = mapped_column(nullable=False)
    Experience: Mapped[int] = mapped_column(nullable=True)
    Paycheck: Mapped[int] = mapped_column()

class Captains(Base):
    __tablename__ = "captains"

    PersonnelNumber: Mapped[str] = mapped_column(primary_key=True)
    Fio: Mapped[str] = mapped_column(nullable=False)
    Experience: Mapped[int] = mapped_column(nullable=True)
    Paycheck: Mapped[int] = mapped_column(nullable=False)

class Cargos(Base):
    __tablename__ = "cargos"

    Id: Mapped[int] = mapped_column(primary_key=True)
    CargoType: Mapped[str] = mapped_column(nullable=False)
    Volume: Mapped[int] = mapped_column(nullable=False)
    Containments: Mapped[str] = mapped_column(nullable=False)
    Weight: Mapped[int] = mapped_column(nullable=False)
    DeliveryCost: Mapped[int] = mapped_column(nullable=False)

class Routes(Base):
    __tablename__ = "routes"

    NumberOfRoute: Mapped[int] = mapped_column(primary_key=True)
    NumberOfStartingPort: Mapped[int] = mapped_column(ForeignKey("ports.Id", ondelete="CASCADE", onupdate="CASCADE"))
    NumberOfEndingPort: Mapped[int] = mapped_column(ForeignKey("ports.Id", ondelete="CASCADE", onupdate="CASCADE"))
    RouteLength: Mapped[int] = mapped_column(nullable=False)

class Cranes(Base):
    __tablename__ = "cranes"

    Id: Mapped[int] = mapped_column(primary_key=True)
    PortNumber: Mapped[int] = mapped_column(ForeignKey("ports.Id", ondelete="CASCADE", onupdate="CASCADE"))
    Experience: Mapped[int] = mapped_column(nullable=False)
    MonthSpendings: Mapped[int] = mapped_column(nullable=False)

class Gates(Base):
    __tablename__ = "gates"

    Id: Mapped[int] = mapped_column(primary_key=True)
    NumberInPort: Mapped[int] = mapped_column(nullable=False)
    NumberOfPort: Mapped[int] = mapped_column(ForeignKey("ports.Id", ondelete="CASCADE", onupdate="CASCADE"))

class Brigades(Base):
    __tablename__ = "brigades"

    Id: Mapped[int] = mapped_column(primary_key=True)
    NumberOfBrigade: Mapped[int] = mapped_column(nullable=False)
    SignedEmployee: Mapped[str] = mapped_column(ForeignKey("loaders.PersonnelNumber", ondelete="CASCADE", onupdate="CASCADE"))

class Cruises(Base):
    __tablename__ = "cruises"

    NumberOfCruise: Mapped[int] = mapped_column(primary_key=True)
    AwaitingDateOfStart: Mapped[datetime] = mapped_column(nullable=False)
    AwaitingDateOfEnd: Mapped[datetime] = mapped_column(nullable=False)
    ActualDateOfStart: Mapped[datetime] = mapped_column(nullable=False)
    ActualDateOfEnd: Mapped[datetime] = mapped_column(nullable=False)
    Ship: Mapped[int] = mapped_column(ForeignKey("ships.NumberOfShip", ondelete="CASCADE", onupdate="CASCADE"))
    Captain: Mapped[str] = mapped_column(ForeignKey("captains.PersonnelNumber", ondelete="CASCADE", onupdate="CASCADE"))
    TypeOfCargo: Mapped[str] = mapped_column(nullable=False)
    NumberOfRoute: Mapped[int] = mapped_column(ForeignKey("routes.NumberOfRoute", ondelete="CASCADE", onupdate="CASCADE"))

class Orders(Base):
    __tablename__ = "orders"

    NumberOfOrder: Mapped[int] = mapped_column(primary_key=True)
    NumberOfCargo: Mapped[int] = mapped_column(ForeignKey("cargos.Id", ondelete="CASCADE", onupdate="CASCADE"))
    NumberOfClient: Mapped[int] = mapped_column(ForeignKey("clients.FaceNumber", ondelete="CASCADE", onupdate="CASCADE"))
    NumberOfSupplier: Mapped[int] = mapped_column(ForeignKey("suppliers.FaceNumber", ondelete="CASCADE", onupdate="CASCADE"))
    DateOfOrdering: Mapped[datetime] = mapped_column(nullable=False)
    AwaitingDateOfReceiving: Mapped[datetime] = mapped_column(nullable=False)
    ActualDateOfReceiving: Mapped[datetime] = mapped_column(nullable=False)
    AwaitingDateOfDeliviring: Mapped[datetime] = mapped_column(nullable=False)
    ActualDateOfDeliviring: Mapped[datetime] = mapped_column(nullable=False)
    NumberOfCruise: Mapped[int] = mapped_column(ForeignKey("cruises.NumberOfCruise", ondelete="CASCADE", onupdate="CASCADE"))
    CostOfDelivery: Mapped[int] = mapped_column(nullable=False)

class ScheduleOfGate(Base):
    __tablename__ = "scheduleofgate"

    Id: Mapped[int] = mapped_column(primary_key=True)
    NumberOfServedCruise: Mapped[int] = mapped_column(ForeignKey("cruises.NumberOfCruise", ondelete="CASCADE", onupdate="CASCADE"))
    NumberOfGate: Mapped[int] = mapped_column(ForeignKey("gates.Id", ondelete="CASCADE", onupdate="CASCADE"))
    NumberOfPort: Mapped[int] = mapped_column(ForeignKey("ports.Id", ondelete="CASCADE", onupdate="CASCADE"))
    NumberOfBrigade: Mapped[int] = mapped_column(ForeignKey("brigades.Id", ondelete="CASCADE", onupdate="CASCADE"))
    AwaitingDateStart: Mapped[datetime] = mapped_column(nullable=False)
    AwaitingDateOfEnd: Mapped[datetime] = mapped_column(nullable=False)
    ActualDateOfStart: Mapped[datetime] = mapped_column(nullable=False)
    ActualDateOfEnd: Mapped[datetime] = mapped_column(nullable=False)
    UpOrDown: Mapped[bool] = mapped_column(nullable=False)