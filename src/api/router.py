from fastapi import APIRouter
from fastapi.params import Depends

from src.api.dependencies.dependency_db import get_filter_repository
from src.api.schemas import FilterUpdate, FilterCreate, FilterRead
from src.database.base_repository import BaseRepository
from src.database.models import Filter
from src.pagination import PaginationParams, Pagination

router = APIRouter()

@router.post("/filter/create")
async def create_filter(filter: FilterCreate, filter_repository: BaseRepository[Filter] = Depends(get_filter_repository)):
    return await filter_repository.create(filter.model_dump())

@router.get("/filter/")
async def read_all_filters(
        filter_repository: BaseRepository[Filter] = Depends(get_filter_repository),
        pagination_params: PaginationParams = Depends(PaginationParams)
):
    count = await filter_repository.count()
    items = await filter_repository.get_all(pagination_params.limit, pagination_params.offset)
    return Pagination[FilterRead](
        items=[FilterRead.model_validate(item, from_attributes=True) for item in items],
        count=count,
    )

@router.get("/filter/{id}")
async def read_filter_by_id(id: int, filter_repository: BaseRepository[Filter] = Depends(get_filter_repository)):
    return await filter_repository.get_by_id(id)


@router.patch('/filter/{id}')
async def update_filter(id: int, filter: FilterUpdate, filter_repository: BaseRepository[Filter] = Depends(get_filter_repository)):
    return await filter_repository.update(id, filter.model_dump())

@router.delete('/filter/{id}')
async def delete_filter(id: int, filter_repository: BaseRepository[Filter] = Depends(get_filter_repository)):
    return await filter_repository.delete(id)