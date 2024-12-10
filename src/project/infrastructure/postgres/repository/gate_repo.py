from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.GateSchema import GateSchema
from project.infrastructure.postgres.models import Gates

from project.core.config import settings
from project.core.exceptions import GateNotFound, GateAlreadyExists


class GateRepository:
    _collection: Type[Gates] = Gates

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_gates(
        self,
        session: AsyncSession,
    ) -> list[GateSchema]:
        query = select(self._collection)

        gates = await session.scalars(query)

        return [GateSchema.model_validate(obj=gate) for gate in gates.all()]

    async def get_gate_by_id(self, session: AsyncSession, gate_id: int) -> GateSchema:
        query = select(self._collection).where(self._collection.id == gate_id)
        gate = await session.scalar(query)
        if not gate:
            raise GateNotFound(gate_id)
        return GateSchema.model_validate(obj=gate)

    async def create_gate(self, session:AsyncSession, gate:GateSchema) -> GateSchema:
        query = (insert(self._collection).values(gate.model_dump()).returning(self._collection))
        try:
            created_gate = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise GateAlreadyExists(gate.id)
        return GateSchema.model_validate(obj=created_gate)

    async def update_gate(self, session: AsyncSession, gate_id: int, gate: GateSchema
    ) -> GateSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == gate_id)
            .values(gate.model_dump())
            .returning(self._collection)
        )

        updated_gate = await session.scalar(query)

        if not updated_gate:
            raise GateNotFound(_gate_id=gate_id)

        return GateSchema.model_validate(obj=updated_gate)

    async def delete_gate(
            self,
            session: AsyncSession,
            gate_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == gate_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise GateNotFound(_gate_id=gate_id)