from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.ClientSchema import ClientSchema
from project.infrastructure.postgres.models import Clients

from project.core.config import settings
from project.core.exceptions import ClientNotFound, ClientAlreadyExists


class ClientRepository:
    _collection: Type[Clients] = Clients

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_clients(
        self,
        session: AsyncSession,
    ) -> list[ClientSchema]:
        query = select(self._collection)

        clients = await session.scalars(query)

        return [ClientSchema.model_validate(obj=client) for client in clients.all()]

    async def get_client_by_fn(self, session: AsyncSession, client_fn: int) -> ClientSchema:
        query = select(self._collection).where(self._collection.face_number == client_fn)
        client = await session.scalar(query)
        if not client:
            raise ClientNotFound(client_fn)
        return ClientSchema.model_validate(obj=client)

    async def create_client(self, session:AsyncSession, client:ClientSchema) -> ClientSchema:
        query = (insert(self._collection).values(client.model_dump()).returning(self._collection))
        try:
            created_client = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise ClientAlreadyExists(client.face_number)
        return ClientSchema.model_validate(obj=created_client)

    async def update_client(self, session: AsyncSession, client_fn: int, client: ClientSchema
    ) -> ClientSchema:
        query = (
            update(self._collection)
            .where(self._collection.face_number == client_fn)
            .values(client.model_dump())
            .returning(self._collection)
        )

        updated_client = await session.scalar(query)

        if not updated_client:
            raise ClientNotFound(_client_fn=client_fn)

        return ClientSchema.model_validate(obj=updated_client)

    async def delete_client(
            self,
            session: AsyncSession,
            client_fn: int
    ) -> None:
        query = delete(self._collection).where(self._collection.face_number == client_fn)

        result = await session.execute(query)

        if not result.rowcount:
            raise ClientNotFound(_client_fn=client_fn)