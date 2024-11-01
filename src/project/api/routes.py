from fastapi import APIRouter

from src.project.infrastructure.postgres.repository.user_repo import UserRepository
from src.project.infrastructure.postgres.database import PostgresDatabase
from src.project.schemas.ships import ShipSchema


router = APIRouter()


@router.get("/all_users", response_model=list[ShipSchema])
async def get_all_users() -> list[ShipSchema]:
    user_repo = UserRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await user_repo.check_connection(session=session)
        all_users = await user_repo.get_all_users(session=session)

    return all_users