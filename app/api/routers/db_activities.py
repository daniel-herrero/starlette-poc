from fastapi import APIRouter
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app.crud.crud_db_activity import db_activity_crud
from app.core.database import get_db, engine, Base
from app.serializers.db_activity import DbActivity

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/db_log",
    tags=["db_activity"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[DbActivity])
def read_db_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_activities = db_activity_crud.get_multi(db, skip=skip, limit=limit)
    return db_activities


@router.get("/{db_activity_id}", response_model=DbActivity)
def read_epic(db_activity_id: int, db: Session = Depends(get_db)):
    db_activity = db_activity_crud.get(db, db_activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Epic not found")
    return db_activity
