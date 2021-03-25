from app.crud.Base import CRUDBase
from app.db_models.epic import Epic
from app.serializers.epic import EpicCreate, EpicUpdate


class CRUDEpic(CRUDBase[Epic, EpicCreate, EpicUpdate]):
    pass


epic_crud = CRUDEpic(Epic)
