from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, status

from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.ships import ShipSchema, ShipCreateUpdateSchema
from project.schemas.healthcheck import HealthCheckSchema
from project.core.exceptions import ShipNotFound, ShipAlreadyExists
from project.api.depends import database, user_repo


router = APIRouter()


@router.get("/all_ships", response_model=list[ShipSchema])
async def get_all_users() -> list[ShipSchema]:
    user_repo = UserRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await user_repo.check_connection(session=session)
        all_ships = await user_repo.get_all_ships(session=session)

    return all_ships

@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=status.HTTP_200_OK)
async def check_health() -> HealthCheckSchema:
    async with database.session() as session:
        db_is_ok = await user_repo.check_connection(session=session)
    return HealthCheckSchema(
        db_is_ok=db_is_ok,
    )
