from datetime import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ...core.db.database import Base


class Grant(Base):
    __tablename__ = 'grants'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    image_url: Mapped[str | None] = mapped_column(String, nullable=True)
    grant_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    grant_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    documents: Mapped[str | None] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    implementation_period: Mapped[str | None] = mapped_column(String, nullable=True)
    competition_name: Mapped[str | None] = mapped_column(String, nullable=True)
    contacts: Mapped[str | None] = mapped_column(String, nullable=True)
    url: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
