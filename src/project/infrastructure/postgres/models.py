from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, ForeignKey

from project.infrastructure.postgres.database import Base

class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    ship_type: Mapped[str] = mapped_column(nullable=False)
    max_volume: Mapped[int] = mapped_column(nullable=False)
    max_weight: Mapped[int] = mapped_column(nullable=False)
    speed: Mapped[int] = mapped_column(nullable=False)
    spendings: Mapped[int] = mapped_column(nullable=False)
    fuel_spendings: Mapped[int] = mapped_column(nullable=False)

class Suppliers(Base):
    __tablename__ = "suppliers"

    face_number: Mapped[int] = mapped_column(primary_key=True)
    name_of_the_firm: Mapped[str] = mapped_column(nullable=False)
    accompalience_date: Mapped[datetime] = mapped_column(nullable=True)
    state_or_private: Mapped[bool] = mapped_column(default=False)

class Clients(Base):
    __tablename__ = "clients"

    face_number: Mapped[int] = mapped_column(primary_key=True)
    name_of_the_firm: Mapped[str] = mapped_column(nullable=False)
    accompalience_date: Mapped[datetime] = mapped_column(nullable=True)
    state_or_private: Mapped[bool] = mapped_column(default=False)

class Ports(Base):
    __tablename__ = "ports"

    id: Mapped[int] = mapped_column(primary_key=True)
    town: Mapped[str] = mapped_column(nullable=False)
    month_spendings: Mapped[int] = mapped_column(nullable=False)

class Loaders(Base):
    __tablename__ = "loaders"

    personnel_number: Mapped[str] = mapped_column(primary_key=True)
    fio: Mapped[str] = mapped_column(nullable=False)
    responsobility: Mapped[str] = mapped_column(nullable=False)
    experience: Mapped[int] = mapped_column(nullable=True)
    paycheck: Mapped[int] = mapped_column()

class Captains(Base):
    __tablename__ = "captains"

    personnel_number: Mapped[str] = mapped_column(primary_key=True)
    fio: Mapped[str] = mapped_column(nullable=False)
    experience: Mapped[int] = mapped_column(nullable=True)
    paycheck: Mapped[int] = mapped_column(nullable=False)

class Cargos(Base):
    __tablename__ = "cargos"

    id: Mapped[int] = mapped_column(primary_key=True)
    cargo_type: Mapped[str] = mapped_column(nullable=False)
    volume: Mapped[int] = mapped_column(nullable=False)
    containments: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[int] = mapped_column(nullable=False)
    delivery_cost: Mapped[int] = mapped_column(nullable=False)

class Routes(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_of_starting_port: Mapped[int] = mapped_column(ForeignKey("ports.id", ondelete="CASCADE", onupdate="CASCADE"))
    number_of_ending_port: Mapped[int] = mapped_column(ForeignKey("ports.id", ondelete="CASCADE", onupdate="CASCADE"))
    route_length: Mapped[int] = mapped_column(nullable=False)

class Cranes(Base):
    __tablename__ = "cranes"

    id: Mapped[int] = mapped_column(primary_key=True)
    port_number: Mapped[int] = mapped_column(ForeignKey("ports.id", ondelete="CASCADE", onupdate="CASCADE"))
    experience: Mapped[int] = mapped_column(nullable=False)
    month_spendings: Mapped[int] = mapped_column(nullable=False)

class Gates(Base):
    __tablename__ = "gates"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_in_port: Mapped[int] = mapped_column(nullable=False)
    number_of_port: Mapped[int] = mapped_column(ForeignKey("ports.id", ondelete="CASCADE", onupdate="CASCADE"))

class Brigades(Base):
    __tablename__ = "brigades"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_of_brigade: Mapped[int] = mapped_column(nullable=False)
    signed_employee: Mapped[str] = mapped_column(ForeignKey("loaders.personnel_number", ondelete="CASCADE", onupdate="CASCADE"))

class Cruises(Base):
    __tablename__ = "cruises"

    id: Mapped[int] = mapped_column(primary_key=True)
    awaiting_date_of_start: Mapped[datetime] = mapped_column(nullable=False)
    awaiting_date_of_end: Mapped[datetime] = mapped_column(nullable=False)
    actual_date_of_start: Mapped[datetime] = mapped_column(nullable=False)
    actual_date_of_end: Mapped[datetime] = mapped_column(nullable=False)
    ship: Mapped[int] = mapped_column(ForeignKey("ships.id", ondelete="CASCADE", onupdate="CASCADE"))
    captain: Mapped[str] = mapped_column(ForeignKey("captains.personnel_number", ondelete="CASCADE", onupdate="CASCADE"))
    type_of_cargo: Mapped[str] = mapped_column(nullable=False)
    number_of_route: Mapped[int] = mapped_column(ForeignKey("routes.id", ondelete="CASCADE", onupdate="CASCADE"))

class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_of_cargo: Mapped[int] = mapped_column(ForeignKey("cargos.id", ondelete="CASCADE", onupdate="CASCADE"))
    number_of_client: Mapped[int] = mapped_column(ForeignKey("clients.face_number", ondelete="CASCADE", onupdate="CASCADE"))
    number_of_supplier: Mapped[int] = mapped_column(ForeignKey("suppliers.face_number", ondelete="CASCADE", onupdate="CASCADE"))
    date_of_ordering: Mapped[datetime] = mapped_column(nullable=False)
    awaiting_date_of_receiving: Mapped[datetime] = mapped_column(nullable=False)
    actual_date_of_receiving: Mapped[datetime] = mapped_column(nullable=False)
    awaiting_date_of_deliviring: Mapped[datetime] = mapped_column(nullable=False)
    actual_date_of_deliviring: Mapped[datetime] = mapped_column(nullable=False)
    number_of_cruise: Mapped[int] = mapped_column(ForeignKey("cruises.id", ondelete="CASCADE", onupdate="CASCADE"))
    cost_of_delivery: Mapped[int] = mapped_column(nullable=False)

class ScheduleOfGate(Base):
    __tablename__ = "scheduleofgate"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_of_served_cruise: Mapped[int] = mapped_column(ForeignKey("cruises.id", ondelete="CASCADE", onupdate="CASCADE"))
    number_of_gate: Mapped[int] = mapped_column(ForeignKey("gates.id", ondelete="CASCADE", onupdate="CASCADE"))
    number_of_port: Mapped[int] = mapped_column(ForeignKey("ports.id", ondelete="CASCADE", onupdate="CASCADE"))
    number_of_brigade: Mapped[int] = mapped_column(ForeignKey("brigades.id", ondelete="CASCADE", onupdate="CASCADE"))
    awaiting_date_of_start: Mapped[datetime] = mapped_column(nullable=False)
    awaiting_date_of_end: Mapped[datetime] = mapped_column(nullable=False)
    actual_date_of_start: Mapped[datetime] = mapped_column(nullable=False)
    actual_date_of_end: Mapped[datetime] = mapped_column(nullable=False)
    up_or_down: Mapped[bool] = mapped_column(nullable=False)