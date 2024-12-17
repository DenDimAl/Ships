from typing import Annotated

from jose import jwt
from jose import JWTError
from fastapi import Depends, HTTPException, status
from project.core.exceptions import CredentialsException

from project.infrastructure.postgres.repository.ship_repo import ShipRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.infrastructure.postgres.repository.captain_repo import CaptainRepository
from project.infrastructure.postgres.repository.loader_repo import LoaderRepository
from project.infrastructure.postgres.repository.client_repo import ClientRepository
from project.infrastructure.postgres.repository.supplier_repo import SupplierRepository
from project.infrastructure.postgres.repository.cargo_repo import CargoRepository
from project.infrastructure.postgres.repository.brigade_repo import BrigadeRepository
from project.infrastructure.postgres.repository.port_repo import PortRepository
from project.infrastructure.postgres.repository.crane_repo import CraneRepository
from project.infrastructure.postgres.repository.gate_repo import GateRepository
from project.infrastructure.postgres.repository.route_repo import RouteRepository
from project.infrastructure.postgres.repository.cruise_repo import CruiseRepository
from project.infrastructure.postgres.repository.order_repo import OrderRepository
from project.infrastructure.postgres.repository.scheduleofgate_repo import ScheduleRepository
from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.resource.auth import oauth2_scheme
from project.schemas.auth import TokenData
from project.schemas.UserSchema import UserSchema
from project.core.config import settings
user_repo = UserRepository()
schedule_repo = ScheduleRepository()
order_repo = OrderRepository()
cruise_repo = CruiseRepository()
route_repo = RouteRepository()
gate_repo = GateRepository()
crane_repo = CraneRepository()
port_repo = PortRepository()
brig_repo = BrigadeRepository()
cargo_repo = CargoRepository()
sup_repo = SupplierRepository()
client_repo = ClientRepository()
load_repo = LoaderRepository()
ship_repo = ShipRepository()
cap_repo = CaptainRepository()
database = PostgresDatabase()

AUTH_EXCEPTION_MESSAGE = "Невозможно проверить данные для авторизации"

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_AUTH_KEY.get_secret_value(),
            algorithms=[settings.AUTH_ALGORITHM],
        )
        username: str = payload.get("sub")
        if username is None:
            raise CredentialsException(detail=AUTH_EXCEPTION_MESSAGE)
        token_data = TokenData(username=username)
    except JWTError:
        raise CredentialsException(detail=AUTH_EXCEPTION_MESSAGE)

    async with database.session() as session:
        user = await user_repo.get_user_by_email(
            session=session,
            email=token_data.username,
        )

    if user is None:
        raise CredentialsException(detail=AUTH_EXCEPTION_MESSAGE)

    return user


def check_for_admin_access(user: UserSchema) -> None:
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Только админ имеет права добавлять/изменять/удалять пользователей"
        )