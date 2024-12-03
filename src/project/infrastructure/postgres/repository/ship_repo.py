from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.ships import ShipSchema
from project.infrastructure.postgres.models import Ship

from project.core.config import settings
from project.core.exceptions import ShipNotFound, ShipAlreadyExists


class ShipRepository:
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

        ships = await session.scalars(query)

        return [ShipSchema.model_validate(obj=ship) for ship in ships.all()]

    async def get_ship_by_id(self, session: AsyncSession,ship_id: int) -> ShipSchema:
        query = select(self._collection).where(self._collection.NumberOfShip == ship_id)
        ship = await session.scalar(query)
        if not ship:
            raise ShipNotFound(ship_id)
        return ShipSchema.model_validate(obj=ship)

    async def create_ship (self, session:AsyncSession, ship:ShipSchema) -> ShipSchema:
        query = (insert(self._collection).values(ship.model_dump()).returning(self._collection))
        try:
            created_ship = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise ShipAlreadyExists(ship.NumberOfShip)
        return ShipSchema.model_validate(obj=created_ship)

    async def update_ship(self, session: AsyncSession, ship_id: int, ship: ShipSchema
    ) -> ShipSchema:
        query = (
            update(self._collection)
            .where(self._collection.NumberOfShip == ship_id)
            .values(ship.model_dump())
            .returning(self._collection)
        )

        updated_ship = await session.scalar(query)

        if not updated_ship:
            raise ShipNotFound(_NumberOfShip=ship_id)

        return ShipSchema.model_validate(obj=updated_ship)

    async def delete_ship(
            self,
            session: AsyncSession,
            ship_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.NumberOfShip == ship_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise ShipNotFound(_NumberOfShip=ship_id)