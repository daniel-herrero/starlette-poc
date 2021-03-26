from typing import List, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from app.api.common_responses import error_response
from app.crud.crud_users import users_crud
from app.core.database import get_db
from app import serializers, validators

router = APIRouter()


@router.get("/", response_model=List[serializers.UserFull])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = users_crud.get_multi(db, skip=skip, limit=limit)

    return users


@router.get("/{user_id}", response_model=serializers.UserFull)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users_crud.get(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.patch("/", response_model=serializers.UserFull)
async def create_user(user_in: validators.UserCreateVal, db: Session = Depends(get_db)):
    """
    Create new user.
    """
    user_same_email = users_crud.get_by_email(db, email=user_in.email)
    user_same_username = users_crud.get_by_username(db, username=user_in.username)
    if user_same_username or user_same_email:
        return JSONResponse(
            error_response("existing.user.error", "The user with this username/email already exists in the system."),
            status_code=400)

    user = users_crud.create(db, obj_in=user_in)

    # To avoid using the response model and return a serializer according to a given parameter
    # if zoom_level_1:
    #   return serializers.UserPartial.from_orm(user)
    # return serializers.UserFull.from_orm(user)
    # Another option: https://github.com/tiangolo/fastapi/issues/1947

    return user
