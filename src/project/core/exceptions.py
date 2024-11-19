from typing import Final

class ShipNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Корабль с номером {NumberOfShip} не найден"
    message: str

    def __init__(self, _NumberOfShip:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(NumberOfShip = _NumberOfShip)
        super().__init__(self.message)

class ShipAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Корабль с номером {NumberOfShip} уже существует"

    def __init__(self, _NumberOfShip:int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(NumberOfShip = _NumberOfShip)
        super().__init__(self.message)