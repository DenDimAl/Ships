from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.ships import ShipSchema, ShipCreateUpdateSchema
from project.infrastructure.postgres.models import Ship

from project.core.config import settings
from project.core.exceptions import ShipNotFound, ShipAlreadyExists


class UserRepository:
    _collection: Type[Ship] = Ship

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_ships(
        self,
        session: AsyncSession,
    ) -> list[ShipSchema]:
        query = select(self._collection)

        ships = await session.execute(text(query))

        return [ShipSchema.model_validate(obj=ship) for ship in ships.mappings().all()]