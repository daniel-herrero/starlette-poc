from fastapi import APIRouter

from .endpoints import epics, userstories, users, projects, websocket, tasks

api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(userstories.router)
api_router.include_router(projects.router)
api_router.include_router(epics.router)
api_router.include_router(tasks.router)
api_router.include_router(websocket.router)
