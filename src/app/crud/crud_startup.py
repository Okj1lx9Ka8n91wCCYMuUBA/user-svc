from fastcrud import FastCRUD
from ..models.startup import Startup  # Импортируем вашу модель Startup
from ..schemas.startup import (
    StartupCreate,
    StartupUpdate,
    StartupRead,
    StartupDelete
)

CRUDStartup = FastCRUD[
    Startup,
    StartupCreate,
    StartupUpdate,
    StartupRead,
    StartupDelete
]
crud_startup = CRUDStartup(Startup)
