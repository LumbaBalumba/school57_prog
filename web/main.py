from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse, HTMLResponse


class User(BaseModel):
    name: str
    age: int
    gender: str
    phone: str


app = FastAPI()


@app.get("/")
async def home():
    return HTMLResponse(
        content="""
        <html>
        <head>
<style>
body {
  color: brown;
}
</style>
</head>
<body>
            <h1 style="color: 55FF00;"> Hello world </h1>
        </body>
        </html>
    """
    )


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    print(user_id)
    return JSONResponse({"user_id": user_id})


@app.post("/users/new/{user_id}")
async def create_user(user: User, user_id: int):
    return JSONResponse({"user": user.name})
