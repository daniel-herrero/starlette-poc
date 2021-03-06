from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.Base import CRUDBase
from app.db_models.task import Task
from app.serializers.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def create_with_assigned(
            self, db: Session, *, obj_in: TaskCreate, user_to_assign: int
    ) -> Task:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, assigned_to=user_to_assign)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


task_crud = CRUDTask(Task)
