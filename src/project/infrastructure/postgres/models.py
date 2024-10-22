from sqlalchemy.orm import Mapped, mapped_column

from src.project.infrastructure.postgres.database import Base

class Ship(Base):
    __tablename__ = "ships"

    NumberOfShip: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(nullable=True)
    ShipType: Mapped[str] = mapped_column(nullable=False)
    Speed: Mapped[int] = mapped_column(nullable=False)
    Spendings: Mapped[int] = mapped_column(nullable=False)
    FuelSpendings: Mapped[int] = mapped_column(nullable=False)
#То же самое?