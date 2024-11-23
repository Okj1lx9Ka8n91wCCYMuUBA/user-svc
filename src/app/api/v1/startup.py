from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from ...core.db.database import SessionLocal
from ...models.startup import Startup
from ...schemas.startup import StartupCreate, StartupRead, StartupUpdate, StartupDelete
from fastcrud import FastCRUD

app = FastAPI()

CRUDStartup = FastCRUD[
    Startup,
    StartupCreate,
    StartupUpdate,
    StartupRead,
    StartupDelete
]
crud_startup = CRUDStartup(Startup)

@app.post("/startups/", response_model=StartupRead)
def create_startup(startup: StartupCreate, db: Session = SessionLocal()):
    return crud_startup.create(startup, db)

@app.get("/startups/{startup_id}", response_model=StartupRead)
def read_startup(startup_id: int, db: Session = SessionLocal()):
    startup = crud_startup.read(startup_id, db)
    if not startup:
        raise HTTPException(status_code=404, detail="Startup not found")
    return startup

@app.put("/startups/{startup_id}", response_model=StartupRead)
def update_startup(startup_id: int, startup: StartupUpdate, db: Session = SessionLocal()):
    updated_startup = crud_startup.update(startup_id, startup, db)
    if not updated_startup:
        raise HTTPException(status_code=404, detail="Startup not found")
    return updated_startup

@app.delete("/startups/{startup_id}", response_model=StartupDelete)
def delete_startup(startup_id: int, db: Session = SessionLocal()):
    result = crud_startup.delete(startup_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="Startup not found")
    return {"detail": "Startup deleted"}
