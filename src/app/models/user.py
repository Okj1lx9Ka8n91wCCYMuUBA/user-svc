import uuid as uuid_pkg
from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import DateTime, ForeignKey, String, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base


class UserType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    ORGANIZATION = "ORGANIZATION"


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)

    # basic fields (required)
    name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    uuid: Mapped[uuid_pkg.UUID] = mapped_column(default_factory=uuid_pkg.uuid4, primary_key=True, unique=True)

    # fields with defaults
    user_type: Mapped[UserType] = mapped_column(
        SQLAlchemyEnum(UserType),
        default=UserType.INDIVIDUAL,
        nullable=False
    )
    profile_image_url: Mapped[str] = mapped_column(String, default="https://profileimageurl.com")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    # nullable fields
    inn: Mapped[str | None] = mapped_column(String(12), unique=True, index=True, nullable=True, default=None)
    organization_name: Mapped[str | None] = mapped_column(String(100), nullable=True, default=None)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    tier_id: Mapped[int | None] = mapped_column(ForeignKey("tier.id"), index=True, default=None, init=False)
