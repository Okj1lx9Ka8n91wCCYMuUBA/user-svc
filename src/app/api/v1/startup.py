from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.db.database import async_get_db
from ...schemas.startup import StartupCreate, StartupRead, StartupUpdate, StartupDelete
from ...crud.crud_startup import crud_startup

router = APIRouter(tags=["startups"])


@router.post("/startups/", response_model=StartupRead)
def create_startup(startup: StartupCreate, db: Annotated[AsyncSession, Depends(async_get_db)]):
    return crud_startup.create(startup, db)


@router.get("/startups/{startup_id}", response_model=StartupRead)
def read_startup(startup_id: int, db: Annotated[AsyncSession, Depends(async_get_db)]):
    startup = crud_startup.read(startup_id, db)
    if not startup:
        raise HTTPException(status_code=404, detail="Startup not found")
    return startup


@router.put("/startups/{startup_id}", response_model=StartupRead)
def update_startup(startup_id: int, startup: StartupUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]):
    updated_startup = crud_startup.update(startup_id, startup, db)
    if not updated_startup:
        raise HTTPException(status_code=404, detail="Startup not found")
    return updated_startup


@router.delete("/startups/{startup_id}", response_model=StartupDelete)
def delete_startup(startup_id: int, db: Annotated[AsyncSession, Depends(async_get_db)]):
    result = crud_startup.delete(startup_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="Startup not found")
    return {"detail": "Startup deleted"}
