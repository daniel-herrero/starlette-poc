from fastapi import APIRouter
from starlette.exceptions import HTTPException

from .. import schemas, crud, models
from ..database import engine, SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/projects/", response_model=List[schemas.ProjectBase])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects


@router.get("/projects/{project_id}", response_model=schemas.ProjectBase)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project