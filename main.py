from api import router as auth_router
from fastapi import FastAPI


app = FastAPI(
    title="JWT Authentication Service",
    description="Service for user registration, login, and token management with JWT.",
    version="1.0.0",
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
