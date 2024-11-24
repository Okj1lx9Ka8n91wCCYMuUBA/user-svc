from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ....core.db.database import async_get_db
from ....crud.pased_data.grant import crud_grant

router = APIRouter(prefix="/parsed_data", tags=["grants"])


@router.get("/grants/")
async def get_grants(
        db: Annotated[AsyncSession, Depends(async_get_db)],
        # skip: int = 0,
        # limit: int = 100
):
    # return await crud_grant.get(db, skip=skip, limit=limit)
    return await crud_grant.get_multi(db)
