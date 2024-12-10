from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.CruiseSchema import CruiseSchema
from project.infrastructure.postgres.models import Cruises

from project.core.config import settings
from project.core.exceptions import CruiseNotFound, CruiseAlreadyExists


class CruiseRepository:
    _collection: Type[Cruises] = Cruises

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_cruises(
        self,
        session: AsyncSession,
    ) -> list[CruiseSchema]:
        query = select(self._collection)

        cruises = await session.scalars(query)

        return [CruiseSchema.model_validate(obj=cruise) for cruise in cruises.all()]

    async def get_cruise_by_id(self, session: AsyncSession, cruise_id: int) -> CruiseSchema:
        query = select(self._collection).where(self._collection.id == cruise_id)
        cruise = await session.scalar(query)
        if not cruise:
            raise CruiseNotFound(cruise_id)
        return CruiseSchema.model_validate(obj=cruise)

    async def create_cruise(self, session:AsyncSession, cruise:CruiseSchema) -> CruiseSchema:
        query = (insert(self._collection).values(cruise.model_dump()).returning(self._collection))
        try:
            created_cruise = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise CruiseAlreadyExists(cruise.id)
        return CruiseSchema.model_validate(obj=created_cruise)

    async def update_cruise(self, session: AsyncSession, cruise_id: int, cruise: CruiseSchema
    ) -> CruiseSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == cruise_id)
            .values(cruise.model_dump())
            .returning(self._collection)
        )

        updated_cruise = await session.scalar(query)

        if not updated_cruise:
            raise CruiseNotFound(_cruise_id=cruise_id)

        return CruiseSchema.model_validate(obj=updated_cruise)

    async def delete_cruise(
            self,
            session: AsyncSession,
            cruise_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == cruise_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise CruiseNotFound(_cruise_id=cruise_id)

