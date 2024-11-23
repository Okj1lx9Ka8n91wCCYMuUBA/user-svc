from datetime import UTC, datetime
from sqlalchemy import DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base

class Startup(Base):
    __tablename__ = "startup"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    startup_id: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)  # Формат S-{номер}
    stage: Mapped[str | None] = mapped_column(String(50), nullable=True)  # Стадия стартапа
    industry: Mapped[str | None] = mapped_column(String(50), nullable=True)  # Индустрия
    revenue: Mapped[int | None] = mapped_column(Integer, nullable=True)  # Выручка
    required_funding: Mapped[int | None] = mapped_column(Integer, nullable=True)  # Необходимое финансирование
    location: Mapped[str | None] = mapped_column(String(100), nullable=True)  # Локация
    work_experience: Mapped[int | None] = mapped_column(Integer, nullable=True)  # Опыт работы
    team_size: Mapped[int | None] = mapped_column(Integer, nullable=True)  # Размер команды
    innovation_focus: Mapped[str | None] = mapped_column(String(50), nullable=True)  # Инновационный фокус
    description: Mapped[str | None] = mapped_column(String(63206), nullable=True)  # Описание стартапа
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))  # Дата создания
