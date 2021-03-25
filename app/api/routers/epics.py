from fastapi import APIRouter
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app.core.database import get_db, engine, Base
from app.crud.crud_epic import epic_crud
from app.serializers.epic import Epic

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/epics",
    tags=["epics"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Epic])
def read_epics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    epics = epic_crud.get_multi(db, skip=skip, limit=limit)
    return epics


@router.get("/{epic_id}", response_model=Epic)
def read_epic(epic_id: int, db: Session = Depends(get_db)):
    db_epic = epic_crud.get(db, epic_id)
    if db_epic is None:
        raise HTTPException(status_code=404, detail="Epic not found")
    return db_epic
