from fastapi import APIRouter
from app import notifier
from starlette.websockets import WebSocket, WebSocketDisconnect


router = APIRouter()


@router.websocket_route("/ws/events")
async def websocket_endpoint(websocket: WebSocket):
    await notifier.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Back event (echo) {websocket.client.host}: '{data}'")
    except WebSocketDisconnect:
        notifier.remove(websocket)


@router.get("/ws/push/{message}")
async def push_to_connected_websockets(message: str):
    await notifier.push(f"! Push notification: {message} !")
