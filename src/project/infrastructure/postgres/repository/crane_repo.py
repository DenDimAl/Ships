from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.CraneSchema import CraneSchema
from project.infrastructure.postgres.models import Cranes

from project.core.config import settings
from project.core.exceptions import CraneNotFound, CraneAlreadyExists


class CraneRepository:
    _collection: Type[Cranes] = Cranes

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_cranes(
        self,
        session: AsyncSession,
    ) -> list[CraneSchema]:
        query = select(self._collection)

        cranes = await session.scalars(query)

        return [CraneSchema.model_validate(obj=crane) for crane in cranes.all()]

    async def get_crane_by_id(self, session: AsyncSession, crane_id: int) -> CraneSchema:
        query = select(self._collection).where(self._collection.id == crane_id)
        crane = await session.scalar(query)
        if not crane:
            raise CraneNotFound(crane_id)
        return CraneSchema.model_validate(obj=crane)

    async def create_crane(self, session:AsyncSession, crane:CraneSchema) -> CraneSchema:
        query = (insert(self._collection).values(crane.model_dump()).returning(self._collection))
        try:
            created_crane = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise CraneAlreadyExists(crane.id)
        return CraneSchema.model_validate(obj=created_crane)

    async def update_crane(self, session: AsyncSession, crane_id: int, crane: CraneSchema
    ) -> CraneSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == crane_id)
            .values(crane.model_dump())
            .returning(self._collection)
        )

        updated_crane = await session.scalar(query)

        if not updated_crane:
            raise CraneNotFound(_crane_id=crane_id)

        return CraneSchema.model_validate(obj=updated_crane)

    async def delete_crane(
            self,
            session: AsyncSession,
            crane_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == crane_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise CraneNotFound(_crane_id=crane_id)