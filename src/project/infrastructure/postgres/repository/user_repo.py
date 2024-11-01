from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.project.schemas.ships import ShipSchema
from src.project.infrastructure.postgres.models import Ship

from src.project.core.config import settings


class UserRepository:
    _collection: Type[Ship] = Ship

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_users(
        self,
        session: AsyncSession,
    ) -> list[ShipSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.users;"

        users = await session.execute(text(query))

        return [ShipSchema.model_validate(obj=user) for user in users.mappings().all()]