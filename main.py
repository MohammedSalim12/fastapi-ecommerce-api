from fastapi import FastAPI
from routs.auth import router as auth_router
from routs.users import router as users_router
from routs.auth_verify import router as verify_router
import database.database_connection

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(verify_router)

@app.get("/")
def home():
    return {"message": "API is running"}
