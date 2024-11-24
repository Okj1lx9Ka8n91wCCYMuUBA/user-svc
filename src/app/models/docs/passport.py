from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from ...core.db.database import Base


class Passport(Base):
    __tablename__ = 'passports'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey('user.uuid'), index=True)

    # base data
    series: Mapped[str | None] = mapped_column(String(4), nullable=True)
    number: Mapped[str | None] = mapped_column(String(6), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String, nullable=True)
    first_name: Mapped[str | None] = mapped_column(String, nullable=True)
    middle_name: Mapped[str | None] = mapped_column(String, nullable=True)
    birth_date: Mapped[str | None] = mapped_column(String, nullable=True)
    birth_place: Mapped[str | None] = mapped_column(String, nullable=True)
    issue_date: Mapped[str | None] = mapped_column(String, nullable=True)
    issuing_authority: Mapped[str | None] = mapped_column(String, nullable=True)
    department_code: Mapped[str | None] = mapped_column(String, nullable=True)

    # registration address
    registration_address: Mapped[str | None] = mapped_column(String, nullable=True)
    registration_date: Mapped[str | None] = mapped_column(String, nullable=True)

    def __init__(self, **kwargs):
        kwargs.pop('id', None)
        super().__init__(**kwargs)
