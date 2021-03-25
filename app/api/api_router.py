from fastapi import APIRouter

from app.api.routers import epics, user_stories, users, projects, websocket, tasks

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})
api_router.include_router(user_stories.router)
api_router.include_router(projects.router)
api_router.include_router(epics.router)
api_router.include_router(tasks.router)
api_router.include_router(websocket.router)
