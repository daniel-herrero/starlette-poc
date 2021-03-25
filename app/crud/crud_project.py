from app.crud.Base import CRUDBase
from app.db_models.project import Project
from app.serializers.project import ProjectCreate, ProjectUpdate


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    pass


project_crud = CRUDProject(Project)
