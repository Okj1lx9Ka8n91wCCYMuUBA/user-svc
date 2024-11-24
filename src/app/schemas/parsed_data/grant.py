from pydantic import BaseModel, ConfigDict


class GrantBase(BaseModel):
    image_url: str | None = None
    grant_min: int | None = None
    grant_max: int | None = None
    documents: str | None = None
    title: str
    description: str | None = None
    implementation_period: str | None = None
    competition_name: str | None = None
    contacts: str | None = None
    url: str | None = None


class GrantCreate(GrantBase):
    model_config = ConfigDict(extra="forbid")


class GrantRead(GrantBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GrantUpdate(GrantBase):
    title: str | None = None  # делаем все поля опциональными для частичного обновления
    model_config = ConfigDict(from_attributes=True)


class GrantUpdateInternal(GrantUpdate):
    pass


class GrantDelete(BaseModel):
    pass
