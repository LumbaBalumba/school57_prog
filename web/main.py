from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from web.db import Database, User

app = FastAPI()

app.mount("/static", StaticFiles(directory="web/static", html=True), name="static")

database = Database()


@app.get("/")
async def home():
    return FileResponse("web/static/html/index.html")


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("web/static/images/favicon.ico")


@app.get("/users/{user_id}/")
async def read_user(user_id: int):
    user = await database.get_user(user_id)
    if user is None:
        return JSONResponse(content={}, status_code=404)
    return JSONResponse(content=user.__dict__)


@app.get("/hello/")
async def hello():
    return FileResponse("web/static/html/hello.html")


@app.post("/users/new/")
async def create_user(user: User):
    user_id = await database.add_user(user)
    return JSONResponse(content={"user_id": user_id}, status_code=200)
