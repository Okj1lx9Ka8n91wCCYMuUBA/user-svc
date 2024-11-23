from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base

class GrantQuestions(Base):
    __tablename__ = 'grant_questions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)  # Используем Mapped и mapped_column
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey('user.uuid'), index=True)  # Связь с пользователем
    requested_amount: Mapped[str] = mapped_column(String, index=True)
    grant_purpose: Mapped[str] = mapped_column(String)
    prepared_documents: Mapped[str] = mapped_column(String)
    patents_or_innovations: Mapped[str] = mapped_column(String)
    previous_grants: Mapped[str] = mapped_column(String)
    operational_regions: Mapped[str] = mapped_column(String)
    business_size: Mapped[str] = mapped_column(String)
    project_idea: Mapped[str] = mapped_column(String)
    annual_revenue: Mapped[str] = mapped_column(String)
    okved_codes: Mapped[str] = mapped_column(String)

    def __init__(self, **kwargs):
        # Удаляем id из kwargs, если он присутствует
        kwargs.pop('id', None)
        super().__init__(**kwargs)
