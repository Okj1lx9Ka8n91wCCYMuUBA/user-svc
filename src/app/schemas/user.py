from datetime import datetime
from typing import Annotated
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

from ..core.schemas import PersistentDeletion, TimestampSchema, UUIDSchema


class UserType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    ORGANIZATION = "ORGANIZATION"


class UserBase(BaseModel):
    username: Annotated[str | None, Field(
        min_length=2,
        max_length=20,
        pattern=r"^[a-zа-яё0-9_-]+$",
        examples=["userson"]
    )] = None

    email: Annotated[EmailStr | None, Field(
        examples=["user.userson@example.com"]
    )] = None

    phone: Annotated[str | None, Field(
        min_length=10,
        max_length=12,
        pattern=r"^\+?\d+$",
        examples=["+79123456789"]
    )] = None

    name: Annotated[str | None, Field(
        min_length=2,
        max_length=150,
        examples=["User Userson"]
    )] = None

    user_type: UserType = UserType.INDIVIDUAL

    # organization fields
    inn: Annotated[str | None, Field(
        min_length=10,
        max_length=12,
        pattern=r"^\d+$",
        examples=["7707083893"]
    )] = None

    profile_image_url: Annotated[str | None, Field(
        pattern=r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",
        examples=["https://example.com/avatar.jpg"]
    )] = None


class User(TimestampSchema, UserBase, UUIDSchema, PersistentDeletion):
    profile_image_url: Annotated[str, Field(default="https://www.profileimageurl.com")]
    hashed_password: str
    is_superuser: bool = False
    tier_id: int | None = None


class UserRead(BaseModel):
    id: int
    uuid: UUID
    name: str | None
    username: str | None
    email: str | None
    phone: str | None
    user_type: UserType
    inn: str | None
    profile_image_url: str | None
    tier_id: int | None


class UserCreate(UserBase):
    model_config = ConfigDict(extra="forbid")
    password: Annotated[str, Field(pattern=r"^.{8,}|[0-9]+|[A-Z]+|[a-z]+|[^a-zA-Z0-9]+$", examples=["Str1ngst!"])]

    @model_validator(mode='after')
    def validate_fields(self):
        if self.user_type == UserType.ORGANIZATION:
            if not self.inn:
                raise ValueError("INN is required for organizations")
            if not self.phone:
                raise ValueError("Phone is required for organizations")
        else:
            if not self.username or not self.email:
                raise ValueError("Username and email are required for individual users")
            if not self.email:
                raise ValueError("Email is required for individual users")
        return self


class UserCreateInternal(UserBase):
    hashed_password: str


class UserUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: Annotated[str | None, Field(min_length=2, max_length=30, examples=["User Userberg"], default=None)]
    username: Annotated[
        str | None, Field(min_length=2, max_length=20, pattern=r"^[a-z0-9]+$", examples=["userberg"], default=None)
    ]
    email: Annotated[EmailStr | None, Field(examples=["user.userberg@example.com"], default=None)]
    profile_image_url: Annotated[
        str | None,
        Field(
            pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", examples=["https://www.profileimageurl.com"], default=None
        ),
    ]


class UserUpdateInternal(UserUpdate):
    updated_at: datetime


class UserTierUpdate(BaseModel):
    tier_id: int


class UserDelete(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_deleted: bool
    deleted_at: datetime


class UserRestoreDeleted(BaseModel):
    is_deleted: bool


class AnonymousSessionCreate(BaseModel):
    device_uuid: Annotated[str, Field(min_length=36, max_length=36)]


class AnonymousSessionResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
