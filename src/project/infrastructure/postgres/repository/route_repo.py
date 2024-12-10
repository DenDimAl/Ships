from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.RouteSchema import RouteSchema
from project.infrastructure.postgres.models import Routes

from project.core.config import settings
from project.core.exceptions import RouteNotFound, RouteAlreadyExists


class RouteRepository:
    _collection: Type[Routes] = Routes

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_routes(
        self,
        session: AsyncSession,
    ) -> list[RouteSchema]:
        query = select(self._collection)

        routes = await session.scalars(query)

        return [RouteSchema.model_validate(obj=route) for route in routes.all()]

    async def get_route_by_id(self, session: AsyncSession, route_id: int) -> RouteSchema:
        query = select(self._collection).where(self._collection.id == route_id)
        route = await session.scalar(query)
        if not route:
            raise RouteNotFound(route_id)
        return RouteSchema.model_validate(obj=route)

    async def create_route(self, session:AsyncSession, route:RouteSchema) -> RouteSchema:
        query = (insert(self._collection).values(route.model_dump()).returning(self._collection))
        try:
            created_route = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise RouteAlreadyExists(route.id)
        return RouteSchema.model_validate(obj=created_route)

    async def update_route(self, session: AsyncSession, route_id: int, route: RouteSchema
    ) -> RouteSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == route_id)
            .values(route.model_dump())
            .returning(self._collection)
        )

        updated_route = await session.scalar(query)

        if not updated_route:
            raise RouteNotFound(_route_id=route_id)

        return RouteSchema.model_validate(obj=updated_route)

    async def delete_route(
            self,
            session: AsyncSession,
            route_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == route_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise RouteNotFound(_route_id=route_id)