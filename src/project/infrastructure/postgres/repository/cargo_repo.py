from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.CargoSchema import CargoSchema
from project.infrastructure.postgres.models import Cargos

from project.core.config import settings
from project.core.exceptions import CargoNotFound, CargoAlreadyExists


class CargoRepository:
    _collection: Type[Cargos] = Cargos

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_cargos(
        self,
        session: AsyncSession,
    ) -> list[CargoSchema]:
        query = select(self._collection)

        cargos = await session.scalars(query)

        return [CargoSchema.model_validate(obj=cargo) for cargo in cargos.all()]

    async def get_cargo_by_id(self, session: AsyncSession, cargo_id: int) -> CargoSchema:
        query = select(self._collection).where(self._collection.id == cargo_id)
        cargo = await session.scalar(query)
        if not cargo:
            raise CargoNotFound(cargo_id)
        return CargoSchema.model_validate(obj=cargo)

    async def create_cargo(self, session:AsyncSession, cargo:CargoSchema) -> CargoSchema:
        query = (insert(self._collection).values(cargo.model_dump()).returning(self._collection))
        try:
            created_cargo = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise CargoAlreadyExists(cargo.id)
        return CargoSchema.model_validate(obj=created_cargo)

    async def update_cargo(self, session: AsyncSession, cargo_id: int, cargo: CargoSchema
    ) -> CargoSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == cargo_id)
            .values(cargo.model_dump())
            .returning(self._collection)
        )

        updated_cargo = await session.scalar(query)

        if not updated_cargo:
            raise CargoNotFound(_cargo_id=cargo_id)

        return CargoSchema.model_validate(obj=updated_cargo)

    async def delete_cargo(
            self,
            session: AsyncSession,
            cargo_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == cargo_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise CargoNotFound(_cargo_id=cargo_id)