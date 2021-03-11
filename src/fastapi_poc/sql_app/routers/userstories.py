from fastapi import APIRouter
from sqlalchemy.orm.exc import StaleDataError
from starlette.exceptions import HTTPException

from .. import schemas, crud, models
from ..database import engine, SessionLocal
from fastapi import Depends, Form
from sqlalchemy.orm import Session

from typing import List
import time


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/userstories/", response_model=List[schemas.UserStoryBase])
def read_userstories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    uss = crud.get_uss(db, skip=skip, limit=limit)
    return uss


@router.get("/userstories/{us_id}", response_model=schemas.UserStoryBase)
def read_us(us_id: int, db: Session = Depends(get_db)):
    db_us = crud.get_us(db, us_id=us_id)
    if db_us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    return db_us


@router.patch("/userstories/{us_id}", response_model=schemas.UserStoryBase)
def update_us_title(us_id: int, subject: str = Form(...), version: int = Form(...), db: Session = Depends(get_db)):
    us = crud.get_us(db, us_id=us_id)
    if us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    else:
        db_us = crud.update_us_subject(db, us, subject, version)
        return db_us


@router.patch("/userstories/{us_id}/sleep/{num_secs}", response_model=schemas.UserStoryBase)
def update_us_title(us_id: int, subject: str = Form(...), version: int = Form(...), num_secs: int = 0,
                    db: Session = Depends(get_db)):
    us = crud.get_us(db, us_id=us_id)
    if us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    else:
        if num_secs is not None:
            time.sleep(num_secs)
        db_us = crud.update_us_subject(db, us, subject, version)
        if isinstance(db_us, StaleDataError):
            return {"error": "Not updated"}
        return db_us