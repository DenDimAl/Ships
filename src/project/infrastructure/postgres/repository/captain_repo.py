from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.CaptainSchema import CaptainSchema
from project.infrastructure.postgres.models import Captains

from project.core.config import settings
from project.core.exceptions import CaptainNotFound, CaptainAlreadyExists


class CaptainRepository:
    _collection: Type[Captains] = Captains

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_captains(
        self,
        session: AsyncSession,
    ) -> list[CaptainSchema]:
        query = select(self._collection)

        caps = await session.scalars(query)

        return [CaptainSchema.model_validate(obj=cap) for cap in caps.all()]

    async def get_captain_by_pn(self, session: AsyncSession,cap_pn: str) -> CaptainSchema:
        query = select(self._collection).where(self._collection.PersonnelNumber == cap_pn)
        cap = await session.scalar(query)
        if not cap:
            raise CaptainNotFound(cap_pn)
        return CaptainSchema.model_validate(obj=cap)

    async def create_captain(self, session:AsyncSession, captain:CaptainSchema) -> CaptainSchema:
        query = (insert(self._collection).values(captain.model_dump()).returning(self._collection))
        try:
            created_cap = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise CaptainAlreadyExists(captain.PersonnelNumber)
        return CaptainSchema.model_validate(obj=created_cap)

    async def update_captain(self, session: AsyncSession, cap_pn: str, cap: CaptainSchema
    ) -> CaptainSchema:
        query = (
            update(self._collection)
            .where(self._collection.PersonnelNumber == cap_pn)
            .values(cap.model_dump())
            .returning(self._collection)
        )

        updated_cap = await session.scalar(query)

        if not updated_cap:
            raise CaptainNotFound(_cap_pn=cap_pn)

        return CaptainSchema.model_validate(obj=updated_cap)

    async def delete_cap(
            self,
            session: AsyncSession,
            cap_pn: str
    ) -> None:
        query = delete(self._collection).where(self._collection.PersonnelNumber == cap_pn)

        result = await session.execute(query)

        if not result.rowcount:
            raise CaptainNotFound(_cap_pn=cap_pn)