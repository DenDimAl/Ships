from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.LoaderSchema import LoaderSchema
from project.infrastructure.postgres.models import Loaders

from project.core.config import settings
from project.core.exceptions import LoaderNotFound, LoaderAlreadyExists


class LoaderRepository:
    _collection: Type[Loaders] = Loaders

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_loaders(
        self,
        session: AsyncSession,
    ) -> list[LoaderSchema]:
        query = select(self._collection)

        loads = await session.scalars(query)

        return [LoaderSchema.model_validate(obj=load) for load in loads.all()]

    async def get_loader_by_pn(self, session: AsyncSession,load_pn: str) -> LoaderSchema:
        query = select(self._collection).where(self._collection.personnel_number == load_pn)
        load = await session.scalar(query)
        if not load:
            raise LoaderNotFound(load_pn)
        return LoaderSchema.model_validate(obj=load)

    async def create_loader(self, session:AsyncSession, loader:LoaderSchema) -> LoaderSchema:
        query = (insert(self._collection).values(loader.model_dump()).returning(self._collection))
        try:
            created_load = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise LoaderAlreadyExists(loader.personnel_number)
        return LoaderSchema.model_validate(obj=created_load)

    async def update_loader(self, session: AsyncSession, load_pn: str, load: LoaderSchema
    ) -> LoaderSchema:
        query = (
            update(self._collection)
            .where(self._collection.personnel_number == load_pn)
            .values(load.model_dump())
            .returning(self._collection)
        )

        updated_load = await session.scalar(query)

        if not updated_load:
            raise LoaderNotFound(_load_pn=load_pn)

        return LoaderSchema.model_validate(obj=updated_load)

    async def delete_loader(
            self,
            session: AsyncSession,
            load_pn: str
    ) -> None:
        query = delete(self._collection).where(self._collection.personnel_number == load_pn)

        result = await session.execute(query)

        if not result.rowcount:
            raise LoaderNotFound(_load_pn=load_pn)