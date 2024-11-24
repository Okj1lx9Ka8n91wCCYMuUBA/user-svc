from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies import get_current_user
from ....core.db.database import async_get_db
from ....crud.docs.passport import crud_passport
from ....schemas.docs.passport import PassportCreate, PassportRead, PassportUpdate
from ....services.doc_ocr import gemini_service

router = APIRouter(prefix="/passport", tags=["passport"])


class PassportRecognitionError(Exception):
    pass


async def validate_passport_data(data: dict) -> bool:
    """Валидация распознанных данных паспорта."""
    required_fields = ['series', 'number', 'last_name', 'first_name']

    # Проверяем наличие обязательных полей
    for field in required_fields:
        if not data.get(field):
            raise PassportRecognitionError(f"Missing required field: {field}")

    # Проверяем формат серии и номера
    if not (data['series'].isdigit() and len(data['series']) == 4):
        raise PassportRecognitionError("Invalid passport series format")

    if not (data['number'].isdigit() and len(data['number']) == 6):
        raise PassportRecognitionError("Invalid passport number format")

    return True


@router.post("/recognize")
async def recognize_passport(
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[AsyncSession, Depends(async_get_db)],
        main_page: UploadFile = File(...),
        registration_page: UploadFile | None = File(None),
):
    try:
        recognized_data = await gemini_service.recognize_passport_data(
            main_page,
            registration_page
        )

        await validate_passport_data(recognized_data)

        passport_data = PassportCreate(
            user_uuid=user.get('uuid'),
            **recognized_data
        )

        return passport_data

    except PassportRecognitionError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error during passport recognition: {str(e)}"
        )


@router.post("/", response_model=PassportRead)
async def create_passport(
        passport_data: PassportCreate,
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[AsyncSession, Depends(async_get_db)],
):
    existing_passport = await crud_passport.get_by(db, user_uuid=user.get('uuid'))
    # if existing_passport:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Passport already exists for this user"
    #     )
    passport_data.user_uuid = user.get('uuid')
    return await crud_passport.create(db, passport_data)


@router.get("/{user_uuid}", response_model=PassportRead)
async def get_passport(
        user: Annotated[dict, Depends(get_current_user)],
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    user_uuid = user.get('uuid')
    passport = await crud_passport.get_by_field(db, "user_uuid", user_uuid)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")
    return passport


@router.put("/{user_uuid}", response_model=PassportRead)
async def update_passport(
        user: Annotated[dict, Depends(get_current_user)],
        passport_data: PassportUpdate,
        db: Annotated[AsyncSession, Depends(async_get_db)]
):
    user_uuid = user.get('uuid')
    passport = await crud_passport.get_by_field(db, "user_uuid", user_uuid)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")
    return await crud_passport.update(db, passport_data, id=passport.id)
