from asyncio import sleep
from datetime import datetime
from typing import List
from deepdiff import DeepDiff

from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from sqlalchemy.orm.exc import StaleDataError

from app import notifier
from app.crud.crud_db_activity import db_activity_crud
from app.crud.crud_user_story import user_story_crud
from app.core.database import engine, get_db, Base
from app.api.common_responses import ws_response
from app import serializers

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/userstories",
    tags=["userstories"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[serializers.UserStory])
async def read_userstories(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    uss = user_story_crud.get_multi(db, skip=skip, limit=limit)
    return uss


@router.get("/{us_id}", response_model=serializers.UserStory)
async def read_us(us_id: int, db: Session = Depends(get_db)):
    db_us = user_story_crud.get(db, us_id)
    if db_us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    return db_us


@router.patch("/{us_id}", response_model=serializers.UserStory)
async def update_us_title(us_id: int, subject: str = Form(...), version: int = Form(...),
                          db: Session = Depends(get_db)):
    # recover the us to update
    us = user_story_crud.get(db, us_id)
    if us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")

    us_s = serializers.UserStory.from_orm(us).dict()
    # writing the updated user story on database
    db_us = user_story_crud.update_us_subject(db, us, subject)

    # calculate the activity changes for the user story
    db_us_s = serializers.UserStory.from_orm(db_us).dict()
    changes = DeepDiff(us_s, db_us_s)

    # write the activity log on database
    db_activity = serializers.DbActivityBase(db=db, created_at=datetime.now(), event="update_us", obj_type="us",
                                             project_id=db_us_s["project"]["id"], obj_id=db_us_s["id"],
                                             obj_changes=changes.to_dict())

    db_activity_crud.create_activity(db, db_activity)

    # send the activity log through websockets
    await notifier.push(ws_response("db_access", "userstory", db_us.id, db_us.project_id, changes))

    return db_us


@router.patch("/{us_id}/sleep/{num_secs}", response_model=serializers.UserStory)
async def update_us_title(us_id: int, subject: str = Form(...), version: int = Form(...), num_secs: int = 0,
                          db: Session = Depends(get_db)):
    us = user_story_crud.get(db, us_id)
    if us is None:
        raise HTTPException(status_code=404, detail="Userstory not found")
    else:
        if num_secs is not None:
            await sleep(num_secs)

        us_s = serializers.UserStory.from_orm(us).dict()
        # writing the updated user story on database
        db_us = user_story_crud.update_us_subject(db, us, subject)
        if isinstance(db_us, StaleDataError):
            return {"error": "Not updated"}
        else:
            # calculate the activity changes for the user story
            db_us_s = serializers.UserStory.from_orm(db_us).dict()
            changes = DeepDiff(us_s, db_us_s)

            # write the activity log on database
            db_activity = serializers.DbActivityBase(db=db, created_at=datetime.now(), event="update_us", obj_type="us",
                                                     project_id=db_us_s["project"]["id"], obj_id=db_us_s["id"],
                                                     obj_changes=changes.to_dict())

            db_activity_crud.create_activity(db, db_activity)

            # send the activity log through websockets
            await notifier.push(ws_response("db_access", "userstory", db_us.id, db_us.project_id, changes))

        return db_us
