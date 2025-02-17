from fastapi import FastAPI
from models import UserIn, UserOut
from auth_service import register_user, authenticate_user  # Updated import

app = FastAPI(title="Sudoku Authentication API")

@app.post("/register", response_model=UserOut)
async def register(user: UserIn):
    return await register_user(user)

@app.post("/login")
async def login(user: UserIn):
    return await authenticate_user(user)

@app.get("/")
async def home():
    return {"message": "Sudoku Authentication Service is running!"}
