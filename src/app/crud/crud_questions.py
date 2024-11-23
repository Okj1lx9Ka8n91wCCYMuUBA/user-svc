from fastcrud import FastCRUD
from ..models.grant_questions import GrantQuestions
from ..schemas.grant_questons import (
    GrantQuestionsCreateInternal,
    GrantQuestionsDelete,
    GrantQuestionsUpdate,
    GrantQuestionsUpdateInternal
)

CRUDGrantQuestions = FastCRUD[
    GrantQuestions,
    GrantQuestionsCreateInternal,
    GrantQuestionsUpdate,
    GrantQuestionsUpdateInternal,
    GrantQuestionsDelete
]
crud_grant_questions = CRUDGrantQuestions(GrantQuestions)
