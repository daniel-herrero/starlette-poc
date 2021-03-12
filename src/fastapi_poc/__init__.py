import json
from notifier import Notifier

notifier = Notifier()


async def send_ws_notification(event: str, obj_type: str, obj_id: int = -1, project_id: int = -1):
    await notifier.push("Back event " + json.dumps(
        {
            "event": event,
            obj_type: {
                "id": obj_id,
                "project_id": project_id,
            }
        }))



