from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.SupplierSchema import SupplierSchema
from project.infrastructure.postgres.models import Suppliers

from project.core.config import settings
from project.core.exceptions import SupplierNotFound, SupplierAlreadyExists


class SupplierRepository:
    _collection: Type[Suppliers] = Suppliers

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_suppliers(
        self,
        session: AsyncSession,
    ) -> list[SupplierSchema]:
        query = select(self._collection)

        suppliers = await session.scalars(query)

        return [SupplierSchema.model_validate(obj=sup) for sup in suppliers.all()]

    async def get_supplier_by_fn(self, session: AsyncSession, supplier_fn: int) -> SupplierSchema:
        query = select(self._collection).where(self._collection.face_number == supplier_fn)
        sup = await session.scalar(query)
        if not sup:
            raise SupplierNotFound(supplier_fn)
        return SupplierSchema.model_validate(obj=sup)

    async def create_supplier(self, session:AsyncSession, supplier:SupplierSchema) -> SupplierSchema:
        query = (insert(self._collection).values(supplier.model_dump()).returning(self._collection))
        try:
            created_supplier = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise SupplierAlreadyExists(supplier.face_number)
        return SupplierSchema.model_validate(obj=created_supplier)

    async def update_supplier(self, session: AsyncSession, supplier_fn: int, supplier: SupplierSchema
    ) -> SupplierSchema:
        query = (
            update(self._collection)
            .where(self._collection.face_number == supplier_fn)
            .values(supplier.model_dump())
            .returning(self._collection)
        )

        updated_sup = await session.scalar(query)

        if not updated_sup:
            raise SupplierNotFound(_sup_fn=supplier_fn)

        return SupplierSchema.model_validate(obj=updated_sup)

    async def delete_supplier(
            self,
            session: AsyncSession,
            supplier_fn: int
    ) -> None:
        query = delete(self._collection).where(self._collection.face_number == supplier_fn)

        result = await session.execute(query)

        if not result.rowcount:
            raise SupplierNotFound(_sup_fn=supplier_fn)