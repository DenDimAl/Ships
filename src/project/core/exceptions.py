from typing import Final

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
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Корабль с номером {cap_pn} уже существует"

    def __init__(self, _cap_pn:str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(cap_pn = _cap_pn)
        super().__init__(self.message)