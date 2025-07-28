from pydantic import BaseModel


class FilterBase(BaseModel):
    car_title: str
    price_up_to: int
    mileage_up_to: int
    year_from: int

class FilterCreate(FilterBase):
    pass

class FilterRead(FilterBase):
    id: int

class FilterUpdate(BaseModel):
    car_title: str | None = None
    price_up_to: int | None = None
    mileage_up_to: int | None = None
    year_from: int | None = None
