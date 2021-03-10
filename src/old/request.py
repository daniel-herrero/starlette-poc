import uvicorn
from starlette.requests import Request
from starlette.responses import Response


# To run execute `$uvicorn request:app`
async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    content = '%s %s' % (request.method, request.url.path)
    response = Response(content, media_type='text/plain')
    await response(scope, receive, send)