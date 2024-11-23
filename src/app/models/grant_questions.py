from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base

class GrantQuestions(Base):
    __tablename__ = 'grant_questions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey('user.uuid'), index=True)
    requested_amount: Mapped[str | None] = mapped_column(String, nullable=True)
    grant_purpose: Mapped[str | None] = mapped_column(String, nullable=True)
    prepared_documents: Mapped[str | None] = mapped_column(String, nullable=True)
    patents_or_innovations: Mapped[str | None] = mapped_column(String, nullable=True)
    previous_grants: Mapped[str | None] = mapped_column(String, nullable=True)
    operational_regions: Mapped[str | None] = mapped_column(String, nullable=True)
    business_size: Mapped[str | None] = mapped_column(String, nullable=True)
    project_idea: Mapped[str | None] = mapped_column(String, nullable=True)
    annual_revenue: Mapped[str | None] = mapped_column(String, nullable=True)
    okved_codes: Mapped[str | None] = mapped_column(String, nullable=True)

    def __init__(self, **kwargs):
        kwargs.pop('id', None)
        super().__init__(**kwargs)
