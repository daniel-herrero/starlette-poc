from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from fastapi_poc import send_ws_notification
from fastapi_poc.sql_app import schemas, crud, models
from fastapi_poc.sql_app.database import get_db


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    await send_ws_notification("database_read", "users")

    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.UserBase)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        await send_ws_notification("database_read", "user", user_id)

    return db_user
