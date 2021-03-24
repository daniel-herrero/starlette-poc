from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.Base import CRUDBase
from app.models.db_activity import DbActivity
from app.schemas.db_activity import DbActivityCreate, DbActivityUpdate, DbActivityInDBBase


class CRUDDbActivity(CRUDBase[DbActivity, DbActivityCreate, DbActivityUpdate]):
    def create_activity(self, db: Session, db_activity: DbActivityCreate):
        db_activity = DbActivity(**db_activity.dict())
        db.add(db_activity)
        db.commit()
        db.refresh(db_activity)


db_activity_crud = CRUDDbActivity(DbActivity)
