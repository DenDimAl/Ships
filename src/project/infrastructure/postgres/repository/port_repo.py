from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.PortSchema import PortSchema
from project.infrastructure.postgres.models import Ports

from project.core.config import settings
from project.core.exceptions import PortNotFound, PortAlreadyExists


class PortRepository:
    _collection: Type[Ports] = Ports

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_ports(
        self,
        session: AsyncSession,
    ) -> list[PortSchema]:
        query = select(self._collection)

        ports = await session.scalars(query)

        return [PortSchema.model_validate(obj=port) for port in ports.all()]

    async def get_port_by_id(self, session: AsyncSession, port_id: int) -> PortSchema:
        query = select(self._collection).where(self._collection.id == port_id)
        cargo = await session.scalar(query)
        if not cargo:
            raise PortNotFound(port_id)
        return PortSchema.model_validate(obj=cargo)

    async def create_port(self, session:AsyncSession, port:PortSchema) -> PortSchema:
        query = (insert(self._collection).values(port.model_dump()).returning(self._collection))
        try:
            created_port = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise PortAlreadyExists(port.id)
        return PortSchema.model_validate(obj=created_port)

    async def update_port(self, session: AsyncSession, port_id: int, port: PortSchema
    ) -> PortSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == port_id)
            .values(port.model_dump())
            .returning(self._collection)
        )

        updated_port = await session.scalar(query)

        if not updated_port:
            raise PortNotFound(_port_id=port_id)

        return PortSchema.model_validate(obj=updated_port)

    async def delete_port(
            self,
            session: AsyncSession,
            port_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == port_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise PortNotFound(_port_id=port_id)