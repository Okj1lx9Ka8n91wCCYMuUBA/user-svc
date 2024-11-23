from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies import get_current_user
from ...core.db.database import async_get_db
from ...crud.crud_questions import crud_grant_questions
from ...schemas.grant_questons import (
    GrantQuestionsCreate,
    GrantQuestionsCreateInternal,
    GrantQuestionsRead,
    GrantQuestionsUpdate
)
from ...schemas.user import UserRead

router = APIRouter(prefix="/grant-questions", tags=["grant_questions"])


@router.post("/", response_model=GrantQuestionsRead)
async def create_grant_questions(
        grant_questions: GrantQuestionsCreate,
        user: Annotated[UserRead, Depends(get_current_user)],
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_uuid = user.get('uuid')
    internal_data = GrantQuestionsCreateInternal(
        **grant_questions.model_dump(),
        user_uuid=user_uuid
    )
    return await crud_grant_questions.create(db, internal_data)


@router.get("/user")
async def get_user_grant_questions(
        db_user: Annotated[UserRead, Depends(get_current_user)],
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    questions = await crud_grant_questions.get_multi(
        db,
        filters={"user_uuid": db_user.get('uuid')}
    )
    if not questions:
        raise HTTPException(status_code=404, detail="Questions not found")
    return questions


@router.get("/{question_id}", response_model=GrantQuestionsRead)
async def get_grant_question(
        question_id: int,
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    question = await crud_grant_questions.get(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.put("/{question_id}", response_model=GrantQuestionsRead)
async def update_grant_question(
        question_id: int,
        update_data: GrantQuestionsUpdate,
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    question = await crud_grant_questions.get(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return await crud_grant_questions.update(db, question_id, update_data)


@router.delete("/{question_id}")
async def delete_grant_question(
        question_id: int,
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    question = await crud_grant_questions.get(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    await crud_grant_questions.delete(db, question_id)
    return {"message": "Question deleted successfully"}
