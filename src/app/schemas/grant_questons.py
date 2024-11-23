# schemas/grant_questions.py
from typing import Annotated
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

class GrantQuestionsBase(BaseModel):
    requested_amount: Annotated[str, Field(examples=["1000000"])]
    grant_purpose: Annotated[str, Field(examples=["Research and Development"])]
    prepared_documents: Annotated[str, Field(examples=["Business Plan, Financial Statements"])]
    patents_or_innovations: Annotated[str, Field(examples=["2 patents pending"])]
    previous_grants: Annotated[str, Field(examples=["None"])]
    operational_regions: Annotated[str, Field(examples=["Moscow, St. Petersburg"])]
    business_size: Annotated[str, Field(examples=["Small"])]
    project_idea: Annotated[str, Field(examples=["Innovative software solution"])]
    annual_revenue: Annotated[str, Field(examples=["5000000"])]
    okved_codes: Annotated[str, Field(examples=["62.01"])]

class GrantQuestionsCreate(GrantQuestionsBase):
    model_config = ConfigDict(extra="forbid")

class GrantQuestionsCreateInternal(GrantQuestionsCreate):
    user_uuid: UUID

class GrantQuestionsRead(GrantQuestionsBase):
    id: int
    user_uuid: UUID

    model_config = ConfigDict(from_attributes=True)

class GrantQuestionsUpdate(BaseModel):
    requested_amount: str | None = None
    grant_purpose: str | None = None
    prepared_documents: str | None = None
    patents_or_innovations: str | None = None
    previous_grants: str | None = None
    operational_regions: str | None = None
    business_size: str | None = None
    project_idea: str | None = None
    annual_revenue: str | None = None
    okved_codes: str | None = None

class GrantQuestionsUpdateInternal(GrantQuestionsUpdate):
    pass

class GrantQuestionsDelete(BaseModel):
    pass
