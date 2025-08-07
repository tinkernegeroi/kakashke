from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.base_repository import BaseRepository
from src.database.database_helper import DatabaseHelper
from src.database.models import Filter


def get_filter_repository(
        session: AsyncSession = Depends(DatabaseHelper.session_depends),
) -> BaseRepository[Filter]:
    return BaseRepository(session, Filter)