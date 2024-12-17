from http.client import HTTPException
from typing import Final

from fastapi import HTTPException, status

class ShipNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Корабль с номером {id} не найден"
    message: str

    def __init__(self, _NumberOfShip:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id = _NumberOfShip)
        super().__init__(self.message)

class ShipAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Корабль с номером {id} уже существует"

    def __init__(self, _NumberOfShip:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id = _NumberOfShip)
        super().__init__(self.message)

class CaptainNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Капитан с номером {cap_pn} не найден"
    message: str

    def __init__(self, _cap_pn:str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cap_pn = _cap_pn)
        super().__init__(self.message)

class CaptainAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Капитан с номером {cap_pn} уже существует"

    def __init__(self, _cap_pn:str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cap_pn = _cap_pn)
        super().__init__(self.message)

class LoaderNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Погрузчик с номером {load_pn} не найден"
    message: str

    def __init__(self, _load_pn:str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(load_pn = _load_pn)
        super().__init__(self.message)

class LoaderAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Погрузчик с номером {cap_pn} уже существует"

    def __init__(self, _load_pn:str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(load_pn = _load_pn)
        super().__init__(self.message)

class ClientNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Клиент с номером {client_fn} не найден"
    message: str

    def __init__(self, _client_fn:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(client_fn = _client_fn)
        super().__init__(self.message)

class ClientAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Клиент с номером {client_fn} уже существует"

    def __init__(self, _client_fn:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(client_fn = _client_fn)
        super().__init__(self.message)

class SupplierNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Поставщик с номером {sup_fn} не найден"
    message: str

    def __init__(self, _sup_fn:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(sup_fn = _sup_fn)
        super().__init__(self.message)

class SupplierAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Поставщик с номером {sup_fn} уже существует"

    def __init__(self, _sup_fn:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(sup_fn = _sup_fn)
        super().__init__(self.message)

class CargoNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Груз с номером {cargo_id} не найден"
    message: str

    def __init__(self, _cargo_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cargo_id = _cargo_id)
        super().__init__(self.message)

class CargoAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Груз с номером {cargo_id} уже существует"

    def __init__(self, _cargo_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cargo_id = _cargo_id)
        super().__init__(self.message)

class BrigadeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Бригада с номером {brigade_id} не найдена"
    message: str

    def __init__(self, _brigade_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(brigade_id = _brigade_id)
        super().__init__(self.message)

class BrigadeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Бригада с номером {brigade_id} уже существует"

    def __init__(self, _brigade_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(brigade_id = _brigade_id)
        super().__init__(self.message)

class PortNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Порт с номером {port_id} не найден"
    message: str

    def __init__(self, _port_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(port_id = _port_id)
        super().__init__(self.message)

class PortAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Порт с номером {port_id} уже существует"

    def __init__(self, _port_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(port_id = _port_id)
        super().__init__(self.message)

class CraneNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Грузовой кран с номером {crane_id} не найден"
    message: str

    def __init__(self, _crane_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(crane_id = _crane_id)
        super().__init__(self.message)

class CraneAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Грузовой кран с номером {crane_id} уже существует"

    def __init__(self, _crane_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(crane_id = _crane_id)
        super().__init__(self.message)

class GateNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Док с номером {gate_id} не найден"
    message: str

    def __init__(self, _gate_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(gate_id = _gate_id)
        super().__init__(self.message)

class GateAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Док с номером {gate_id} уже существует"

    def __init__(self, _gate_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(gate_id = _gate_id)
        super().__init__(self.message)

class RouteNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Маршрут с номером {route_id} не найден"
    message: str

    def __init__(self, _route_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(route_id = _route_id)
        super().__init__(self.message)

class RouteAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Маршрут с номером {route_id} уже существует"

    def __init__(self, _route_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(route_id = _route_id)
        super().__init__(self.message)

class CruiseNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Круиз с номером {cruise_id} не найден"
    message: str

    def __init__(self, _cruise_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cruise_id = _cruise_id)
        super().__init__(self.message)

class CruiseAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Круиз с номером {cruise_id} уже существует"

    def __init__(self, _cruise_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cruise_id = _cruise_id)
        super().__init__(self.message)

class OrderNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Заказ с номером {order_id} не найден"
    message: str

    def __init__(self, _order_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(order_id = _order_id)
        super().__init__(self.message)

class OrderAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Заказ с номером {order_id} уже существует"

    def __init__(self, _order_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(order_id = _order_id)
        super().__init__(self.message)

class ScheduleNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Расписание с номером {schedule_id} не найдено"
    message: str

    def __init__(self, _schedule_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(schedule_id = _schedule_id)
        super().__init__(self.message)

class ScheduleAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Расписание с номером {schedule_id} уже существует"

    def __init__(self, _schedule_id:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(schedule_id = _schedule_id)
        super().__init__(self.message)

class UserNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "User с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class UserAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Пользователь с почтой '{email}' уже существует"

    def __init__(self, email: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(email=email)
        super().__init__(self.message)

class CredentialsException(HTTPException):
    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail=detail,
                         headers = {"WWW-Authenticate": "Bearer"})

class DatabaseError(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Произошла ошибка в базе данных: {message}"

    def __init__(self, message: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(message=message)
        super().__init__(self.message)

