from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict, model_validator

class ProgramBase(BaseModel):
    title: Annotated[str | None, Field(examples=["Студенческий стартап"])] = None
    url: Annotated[str | None, Field(examples=["https://fasie.ru/programs/programma-studstartup/"])] = None
    description: Annotated[str | None, Field(examples=["Поддержка студенческих проектов..."])] = None

class ProgramCreate(ProgramBase):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode='after')
    def validate_at_least_one_field(self) -> 'ProgramCreate':
        fields = [self.title, self.url, self.description]
        if not any(fields):
            raise ValueError("At least one field must be filled")
        return self

class ProgramRead(ProgramBase):
    id: int
    created_at: str  # Можно использовать datetime, если нужно

    model_config = ConfigDict(from_attributes=True)

class ProgramUpdate(BaseModel):
    title: str | None = None
    url: str | None = None
    description: str | None = None

class ProgramDelete(BaseModel):
    pass
