from sqlalchemy.orm import Session

from app.crud.Base import CRUDBase
from app.db_models.user_story import UserStory
from app.serializers.user_stories import UserStoryCreate, UserStoryUpdate


class CRUDUserStory(CRUDBase[UserStory, UserStoryCreate, UserStoryUpdate]):
    def update_us_subject(self, db: Session, db_us: UserStory, subject: str):
        db_us.subject = subject
        db.commit()
        return db_us


user_story_crud = CRUDUserStory(UserStory)
