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
    """User model that supports both individual and organization accounts. Yeah swaaag! 🔥"""
    __tablename__ = "user"

    # required fields without defaults
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    # individual fields
    username: Mapped[str | None] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=True
    )
    email: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=True
    )
    phone: Mapped[str | None] = mapped_column(
        String(12),
        index=True,
        nullable=True
    )

    # organizational fields
    inn: Mapped[str | None] = mapped_column(
        String(12),
        index=True,
        nullable=True
    )
    name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    # system fields with init=false
    id: Mapped[int] = mapped_column(
        "id",
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
        init=False
    )
    tier_id: Mapped[int | None] = mapped_column(
        ForeignKey("tier.id"),
        index=True,
        default=None,
        nullable=True,
        init=False
    )

    # fields with defaults - swagger time!
    user_type: Mapped[UserType] = mapped_column(
        SQLAlchemyEnum(UserType, name="user_type", create_constraint=True, native_enum=True),
        nullable=False,
        default=UserType.INDIVIDUAL
    )
    uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        unique=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default_factory=lambda: datetime.now(UTC),
        nullable=False
    )
    profile_image_url: Mapped[str] = mapped_column(
        String,
        default="https://profileimageurl.com",
        nullable=False
    )
    is_deleted: Mapped[bool] = mapped_column(
        default=False,
        index=True,
        nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )

    # timestamp fields with defaults
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=None,
        nullable=True
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=None,
        nullable=True
    )
