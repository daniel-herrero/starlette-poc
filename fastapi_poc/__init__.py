import json

from notifier import Notifier

notifier = Notifier()


async def send_ws_notification(event: str, obj_type: str, obj_id: int, project_id: int, changes=None):
    await notifier.push("Back event " + json.dumps(
        {
            "event": event,
            "item": {
                "type": obj_type,
                "id": obj_id,
                "proj_id": project_id,
                "changes": changes
            }
        }))
