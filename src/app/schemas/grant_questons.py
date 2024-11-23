# schemas/grant_questions.py
from typing import Annotated
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict, model_validator


class GrantQuestionsBase(BaseModel):
    requested_amount: Annotated[str | None, Field(examples=["1000000"])] = None
    grant_purpose: Annotated[str | None, Field(examples=["Research and Development"])] = None
    prepared_documents: Annotated[str | None, Field(examples=["Business Plan, Financial Statements"])] = None
    patents_or_innovations: Annotated[str | None, Field(examples=["2 patents pending"])] = None
    previous_grants: Annotated[str | None, Field(examples=["None"])] = None
    operational_regions: Annotated[str | None, Field(examples=["Moscow, St. Petersburg"])] = None
    business_size: Annotated[str | None, Field(examples=["Small"])] = None
    project_idea: Annotated[str | None, Field(examples=["Innovative software solution"])] = None
    annual_revenue: Annotated[str | None, Field(examples=["5000000"])] = None
    okved_codes: Annotated[str | None, Field(examples=["62.01"])] = None


class GrantQuestionsCreate(GrantQuestionsBase):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode='after')
    def validate_at_least_one_field(self) -> 'GrantQuestionsCreate':
        fields = [
            self.requested_amount,
            self.grant_purpose,
            self.prepared_documents,
            self.patents_or_innovations,
            self.previous_grants,
            self.operational_regions,
            self.business_size,
            self.project_idea,
            self.annual_revenue,
            self.okved_codes
        ]
        if not any(fields):
            raise ValueError("At least one field must be filled")
        return self

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
