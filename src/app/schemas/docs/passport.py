from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict, model_validator
from uuid import UUID


class PassportBase(BaseModel):
    series: Annotated[str | None, Field(max_length=4)] = None
    number: Annotated[str | None, Field(max_length=6)] = None
    last_name: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    birth_date: str | None = None
    birth_place: str | None = None
    issue_date: str | None = None
    issuing_authority: str | None = None
    department_code: str | None = None
    registration_address: str | None = None
    registration_date: str | None = None


class PassportCreate(PassportBase):
    model_config = ConfigDict(extra="forbid")
    user_uuid: UUID | None = None

    @model_validator(mode='after')
    def validate_required_fields(self) -> 'PassportCreate':
        if not self.user_uuid:
            raise ValueError("user_uuid is required")
        return self


class PassportRead(PassportBase):
    id: int
    user_uuid: UUID | None = None

    model_config = ConfigDict(from_attributes=True)


class PassportUpdate(BaseModel):
    series: str | None = None
    number: str | None = None
    last_name: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    birth_date: str | None = None
    birth_place: str | None = None
    issue_date: str | None = None
    issuing_authority: str | None = None
    department_code: str | None = None
    registration_address: str | None = None
    registration_date: str | None = None


class PassportDelete(BaseModel):
    pass
