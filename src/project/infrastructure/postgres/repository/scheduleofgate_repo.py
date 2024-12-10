from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.ScheduleOfGateSchema import ScheduleOfGateSchema
from project.infrastructure.postgres.models import ScheduleOfGate

from project.core.config import settings
from project.core.exceptions import ScheduleNotFound, ScheduleAlreadyExists


class ScheduleRepository:
    _collection: Type[ScheduleOfGate] = ScheduleOfGate

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_schedules(
        self,
        session: AsyncSession,
    ) -> list[ScheduleOfGateSchema]:
        query = select(self._collection)

        schedules = await session.scalars(query)

        return [ScheduleOfGateSchema.model_validate(obj=schedule) for schedule in schedules.all()]

    async def get_schedule_by_id(self, session: AsyncSession, schedule_id: int) -> ScheduleOfGateSchema:
        query = select(self._collection).where(self._collection.id == schedule_id)
        schedule = await session.scalar(query)
        if not schedule:
            raise ScheduleNotFound(schedule_id)
        return ScheduleOfGateSchema.model_validate(obj=schedule)

    async def create_schedule(self, session:AsyncSession, schedule:ScheduleOfGateSchema) -> ScheduleOfGateSchema:
        query = (insert(self._collection).values(schedule.model_dump()).returning(self._collection))
        try:
            created_schedule = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise ScheduleAlreadyExists(schedule.id)
        return ScheduleOfGateSchema.model_validate(obj=created_schedule)

    async def update_schedule(self, session: AsyncSession, schedule_id: int, schedule: ScheduleOfGateSchema
    ) -> ScheduleOfGateSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == schedule_id)
            .values(schedule.model_dump())
            .returning(self._collection)
        )

        updated_schedule = await session.scalar(query)

        if not updated_schedule:
            raise ScheduleNotFound(_schedule_id=schedule_id)

        return ScheduleOfGateSchema.model_validate(obj=updated_schedule)

    async def delete_schedule(
            self,
            session: AsyncSession,
            schedule_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == schedule_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise ScheduleNotFound(_schedule_id=schedule_id)


