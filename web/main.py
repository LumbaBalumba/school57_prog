from fastapi import FastAPI
from starlette.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from web.db import Database, User
from sys import stderr


app = FastAPI()

app.mount("/static", StaticFiles(directory="web/static", html=True), name="static")

database = Database()


@app.get("/")
async def home():
    return FileResponse("/static/index.html")


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = await database.get_user(user_id)
    if user is None:
        return JSONResponse({}, status_code=404)
    return JSONResponse(user.__dict__)


@app.post("/users/new")
async def create_user(user: User):
    print(user, file=stderr)
    await database.add_user(user)
    return Response(status_code=200)
