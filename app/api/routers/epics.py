from fastapi import APIRouter
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from starlette.exceptions import HTTPException

from app.database.database import get_db, engine
from app.api import crud
from app.schemas import schemas
from app.models import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/epics",
    tags=["epics"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.Epic])
def read_epics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    epics = crud.get_epics(db, skip=skip, limit=limit)
    return epics


@router.get("/{epic_id}", response_model=schemas.Epic)
def read_epic(epic_id: int, db: Session = Depends(get_db)):
    db_epic = crud.get_epic(db, epic_id=epic_id)
    if db_epic is None:
        raise HTTPException(status_code=404, detail="Epic not found")
    return db_epic