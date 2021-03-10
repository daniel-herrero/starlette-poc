from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=List[schemas.UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/userstories/", response_model=List[schemas.UserStoryBase])
def read_userstories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    uss = crud.get_userstories(db, skip=skip, limit=limit)
    return uss


@app.get("/userstories/{us_id}", response_model=schemas.UserStoryBase)
def read_us(us_id: int, db: Session = Depends(get_db)):
    db_us = crud.get_us(db, us_id=us_id)
    if db_us is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_us


