from fastcrud import FastCRUD
from ..models.program import Program  # Импортируем вашу модель Program
from ..schemas.program import (
    ProgramCreate,
    ProgramUpdate,
    ProgramRead,
    ProgramDelete
)

CRUDProgram = FastCRUD[
    Program,
    ProgramCreate,
    ProgramUpdate,
    ProgramRead,
    ProgramDelete
]
crud_program = CRUDProgram(Program)
