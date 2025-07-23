from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base



class Car(Base):
    title: Mapped[str] = mapped_column(index=True)
    year: Mapped[int] = mapped_column(nullable=True)
    full_price: Mapped[int] = mapped_column(nullable=True, index=True)
    monthly_price: Mapped[int] = mapped_column(nullable=True)
    mileage: Mapped[int] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)


class Filter(Base):
    car_title: Mapped[str] = mapped_column(index=True)
    price_up_to: Mapped[int] = mapped_column(nullable=True)
    mileage_up_to: Mapped[int] = mapped_column(nullable=True)
    year_from: Mapped[int] = mapped_column(nullable=True)

