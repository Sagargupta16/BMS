import fastapi as FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from routes import student_routes

app = FastAPI.FastAPI()

app.include_router(student_routes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
