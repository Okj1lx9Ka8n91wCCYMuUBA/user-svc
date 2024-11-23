from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict, model_validator


class StartupBase(BaseModel):
    startup_id: Annotated[str | None, Field(examples=["S-1"])] = None
    stage: Annotated[str | None, Field(examples=["Идея", "Прототип", "Запуск", "Рост", "Зрелость"])] = None
    industry: Annotated[str | None, Field(examples=["Технологии", "Здравоохранение", "Финансы"])] = None
    revenue: Annotated[int | None, Field(examples=[1000000])] = None
    required_funding: Annotated[int | None, Field(examples=[500000])] = None
    location: Annotated[str | None, Field(examples=["Москва", "Санкт-Петербург"])] = None
    work_experience: Annotated[int | None, Field(examples=[3])] = None
    team_size: Annotated[int | None, Field(examples=[10])] = None
    innovation_focus: Annotated[str | None, Field(examples=["На базе ИИ", "Устойчивое развитие"])] = None
    description: Annotated[str | None, Field(examples=["Описание стартапа"])] = None


class StartupCreate(StartupBase):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode='after')
    def validate_at_least_one_field(self) -> 'StartupCreate':
        fields = [
            self.stage,
            self.industry,
            self.revenue,
            self.required_funding,
            self.location,
            self.work_experience,
            self.team_size,
            self.innovation_focus,
            self.description
        ]
        if not any(fields):
            raise ValueError("At least one field must be filled")
        return self


class StartupRead(StartupBase):
    id: int
    created_at: str  # Можно использовать datetime, если нужно

    model_config = ConfigDict(from_attributes=True)


class StartupUpdate(BaseModel):
    stage: str | None = None
    industry: str | None = None
    revenue: int | None = None
    required_funding: int | None = None
    location: str | None = None
    work_experience: int | None = None
    team_size: int | None = None
    innovation_focus: str | None = None
    description: str | None = None


class StartupDelete(BaseModel):
    pass
