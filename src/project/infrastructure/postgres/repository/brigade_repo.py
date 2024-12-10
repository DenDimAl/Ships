from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.BrigadeSchema import BrigadeSchema
from project.infrastructure.postgres.models import Brigades

from project.core.config import settings
from project.core.exceptions import BrigadeNotFound, BrigadeAlreadyExists


class BrigadeRepository:
    _collection: Type[Brigades] = Brigades

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_brigades(
        self,
        session: AsyncSession,
    ) -> list[BrigadeSchema]:
        query = select(self._collection)

        brigades = await session.scalars(query)

        return [BrigadeSchema.model_validate(obj=brig) for brig in brigades.all()]

    async def get_brigade_by_id(self, session: AsyncSession, brig_id: int) -> BrigadeSchema:
        query = select(self._collection).where(self._collection.number_of_brigade == brig_id)
        cargo = await session.scalar(query)
        if not cargo:
            raise BrigadeNotFound(brig_id)
        return BrigadeSchema.model_validate(obj=cargo)

    async def create_brigade(self, session:AsyncSession, brigade:BrigadeSchema) -> BrigadeSchema:
        query = (insert(self._collection).values(brigade.model_dump()).returning(self._collection))
        try:
            created_brig = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise BrigadeAlreadyExists(brigade.id)
        return BrigadeSchema.model_validate(obj=created_brig)

    async def update_brigade(self, session: AsyncSession, brig_id: int, brig: BrigadeSchema
    ) -> BrigadeSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == brig_id)
            .values(brig.model_dump())
            .returning(self._collection)
        )

        updated_brig = await session.scalar(query)

        if not updated_brig:
            raise BrigadeNotFound(_brigade_id=brig_id)

        return BrigadeSchema.model_validate(obj=updated_brig)

    async def delete_brigade(
            self,
            session: AsyncSession,
            brig_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == brig_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise BrigadeNotFound(_brigade_id=brig_id)