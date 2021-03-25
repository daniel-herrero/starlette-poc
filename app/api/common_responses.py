import json


def ws_response(event: str, obj_type: str, obj_id: int, project_id: int, changes=None):
    return "Back event " + json.dumps(
        {
            "event": event,
            "item": {
                "type": obj_type,
                "id": obj_id,
                "proj_id": project_id,
                "changes": changes
            }
        })


def error_response(code: str, message: str, detail: json = {}):
    return {
        "error": {
            "code": code,
            "message": message,
            "detail": detail
        }
    }


def exception_notification(exception):
    return "Back event " + json.dumps(
        {
            "event": "exception",
            "details": {
                "code": "OCC.StaleDataError",
                "text": "Content has been update by another user",
                "message": str(exception),
            }
        }
    )