from datetime import UTC, datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base


class Program(Base):
    __tablename__ = "program"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)  # Заголовок программы
    url: Mapped[str] = mapped_column(String(255), nullable=False)  # URL программы
    description: Mapped[str] = mapped_column(String(63206), nullable=False)  # Описание программы

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 default_factory=lambda: datetime.now(UTC))  # Дата создания
