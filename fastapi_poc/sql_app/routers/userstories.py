import json
from asyncio import sleep
from typing import List
from deepdiff import DeepDiff

from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from sqlalchemy.orm.exc import StaleDataError

from fastapi_poc.sql_app.database import engine
from fastapi_poc.sql_app import schemas, crud, models
from fastapi_poc.sql_app.database import get_db
from fastapi_poc import send_ws_notification

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/userstories",
    tags=["userstories"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.UserStory])
async def read_userstories(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    uss = crud.get_uss(db, skip=skip, limit=limit)
    return uss


@router.get("/{us_id}", response_model=schemas.UserStory)
async def read_us(us_id: int, db: Session = Depends(get_db)):
    db_us = crud.get_us(db, us_id=us_id)
    if db_us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    return db_us


@router.patch("/{us_id}", response_model=schemas.UserStory)
async def update_us_title(us_id: int, subject: str = Form(...), version: int = Form(...),
                          db: Session = Depends(get_db)):
    us = crud.get_us(db, us_id=us_id)
    if us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    else:
        us_s = schemas.UserStory.from_orm(us).dict()
        db_us = crud.update_us_subject(db, us, subject, version)
        db_us_s = schemas.UserStory.from_orm(db_us).dict()
        changes = DeepDiff(us_s, db_us_s)

        await send_ws_notification("db_access", "userstory", db_us.id, db_us.project_id, changes)

        return db_us


@router.patch("/{us_id}/sleep/{num_secs}", response_model=schemas.UserStory)
async def update_us_title(us_id: int, subject: str = Form(...), version: int = Form(...), num_secs: int = 0,
                          db: Session = Depends(get_db)):
    us = crud.get_us(db, us_id=us_id)
    if us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    else:
        if num_secs is not None:
            await sleep(num_secs)
        us_s = schemas.UserStory.from_orm(us).dict()
        db_us = crud.update_us_subject(db, us, subject, version)
        if isinstance(db_us, StaleDataError):
            return {"error": "Not updated"}
        else:
            db_us_s = schemas.UserStory.from_orm(db_us).dict()
            changes = DeepDiff(us_s, db_us_s)

            await send_ws_notification("db_access", "userstory", db_us.id, db_us.project_id, changes)

        return db_us
