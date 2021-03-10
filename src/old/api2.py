import asyncio
import uvicorn
# import orm

from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse, HTMLResponse, StreamingResponse, Response, \
    RedirectResponse
from starlette.routing import Route, WebSocketRoute, Mount

# HTML Response
from starlette.schemas import SchemaGenerator
from starlette.staticfiles import StaticFiles

import taigadb

# Configuration for OpenApi documentation
schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)

# HTTP/2 and HTTP/3 server push (push resources to the client to speed up page load time)
async def homepage(request):
    """
    Homepage which uses server push to deliver the stylesheet.
    """
    await request.send_push_promise("/statics/css/bootstrap.min.css")
    return HTMLResponse(
        '<html><head><link rel="stylesheet" href="/statics/css/bootstrap.min.css"/><h1>Hello, world!</h1></head></html>'
    )


# Plain Text Response
# Accessing the application state from the Request
async def user_me(request):
    username = request.app.state.ADMIN_NAME
    email = request.app.state.ADMIN_EMAIL
    return PlainTextResponse('Hello, %s! (%s)' % (username, email))


# JSON Response
# Taking params from the Request
async def user(request):
    username = request.path_params['username']
    content = '%s %s' % (request.method, request.url.path)
    return JSONResponse(
        {
            'request': {
                'method': request.method,
                'url_path': request.url.path,
                'ip': request.client.host,
            },
            'message': 'Hello, %s!' % username
        })


# Streaming the HTML response body from ... (1/2)
def numbers(request):
    generator = slow_numbers(1, 10)
    return StreamingResponse(generator, media_type='text/html')


# ... an async HTML generator (2/2)
async def slow_numbers(minimum, maximum):
    yield ('<html><body><ul>')
    for number in range(minimum, maximum + 1):
        yield '<li>%d</li>' % number
        await asyncio.sleep(3)
    yield ('</ul></body></html>')


# A listening Websocket
async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()


# Open issue when setting a cookie, so ... a 500 Error instead
#   https://github.com/encode/starlette/issues/791
async def set_cookie(request):
    await Response.set_cookie("cookie", "galleta", max_age=None, expires=None, path="/", domain=None, secure=False,
                        httponly=False, samesite="lax")
    return PlainTextResponse('Cookie set!')


# Redirections (not a 203, but a `307 Temporary Redirect`)
def redirection(request):
    return RedirectResponse(url='/')


# Executing SQLs to the DATABASE (1/2)
async def get_query_results(ddbb, query: str):
    rows = await ddbb.fetch_all(query=query)
    return rows


# DATABASE access: listing Taiga's users (from postgresql) (2/2)
async def list_users(request):
    # OpenAPI schemas based on the docstrings
    """
    responses:
        200:
            description: A list of users.
            examples:
                [{"id": 13,"username": "user7","email": "user7@taigaio.demo"},
                {"id": 5,"username": "taiga","email": "daniel.herrero@kaleidos.net"}]
    """
    query_result = await get_query_results(taigadb.Taiga_db, taigadb.users_query)
    content = [
        {
            "id": result["id"],
            "username": result["username"],
            "email": result["email"],
        }
        for result in query_result
    ]
    return JSONResponse(content)


async def update_us(request):
    us_id = request.path_params['id']
    form = await request.form()
    print(form['subject'])
    print(form['version'])

    us = taigadb.get_us_by_id(int(us_id))
    us.subject = form['subject']
    us.version = form['version']

    taigadb.commit_changes()

    return JSONResponse(us.to_dict())

# Same query using SQLAlchemy  (2/2)
async def list_projects_alchemy(request):
    # OpenAPI schemas based on the docstrings
    """
    responses:
        200:
            description: A list of projects.
            examples:
                [{"id": 9,"name": "Scrum project 001","description": "Scrum project 001"},
                {"id": 4, "name": "Project Example 4","description": "Project example 4 description"}]
    """
    results = await taigadb.Taiga_db.fetch_all(taigadb.all_projects_query)
    content = [
        dict(result)
        for result in results
    ]
    return JSONResponse(content)


# Api schema
def openapi_schema(request):
    api_schema = schemas.get_schema(routes=app.routes)
    print(app.routes)
    print(api_schema)
    return JSONResponse(api_schema)


# Code executed when the Uvicorn server starts
def startup_msg():
    print('Starting the POC!')


# Code executed when the Uvicorn server exits
def shutdown_msg():
    print('See you soon!')

# Event handler when starting the app
async def some_startup_task():
    print('Prior to serve any incoming requests, I\'ll do some work ...')
    await asyncio.sleep(2)

# Event handler when stoppping the app
async def some_shutdown_task():
    print('I have to do some things, just a sec ...')
    await asyncio.sleep(1)

routes = [
    Route('/', homepage),
    Route('/user/me', user_me, methods=["GET", "POST"]),
    Route('/user/{username}', user),
    Route('/numbers', numbers),
    Route('/set_cookie', set_cookie),
    Route('/redirection', redirection),
    Route("/taiga/schema", endpoint=openapi_schema, include_in_schema=True),
    Route("/taiga/users", list_users),
    Route("/taiga/sqlalchemy/projects", list_projects_alchemy),
    Route("/api2/v1/userstories/{id}", update_us, methods=["PATCH"]),
    WebSocketRoute('/ws', websocket_endpoint),
    # Serving just the STATIC FILES in path /statics/png (e.g. not '/statics/one-png', but '/statics/png/one-png')
    Mount("/statics", app=StaticFiles(directory="statics"), name="statics")
]

# Starlette configuration: Endpoints, start/stop scripts, debuging on 500
app = Starlette(debug=True,
                on_startup=[taigadb.Taiga_db.connect, startup_msg],
                on_shutdown=[taigadb.Taiga_db.disconnect, shutdown_msg],
                routes=routes)

# Defining variables in the application state
app.state.ADMIN_EMAIL = 'daniel.herrero@kaleidos.net'
app.state.ADMIN_NAME = 'Daniel Herrero'

# It allows to launch Uvicorn from python3 (Execute:  `$python3 example.py`)
# If not, it has to be launched with uvicorn (`$ uvicorn example:app`)
if __name__ == "__main__":
    uvicorn.run("api2:app", host="127.0.0.1", port=10000, log_level="info")