from project.infrastructure.postgres.repository.ship_repo import ShipRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.infrastructure.postgres.repository.captain_repo import CaptainRepository
ship_repo = ShipRepository()
cap_repo = CaptainRepository()
database = PostgresDatabase()