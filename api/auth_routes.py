from fastapi import APIRouter, Depends, HTTPException, status
from .schemes import UserInfoRequest, JwtResponse, JwtAccessResponse, UserInfoResponse
from db import get_db, create_user, find_user_by_email
from sqlalchemy.ext.asyncio import AsyncSession
from core import (
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
    verify_access_token,
)

router = APIRouter()


@router.post(
    "/register/",
    summary="Register a new user",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(user_reg: UserInfoRequest, db: AsyncSession = Depends(get_db)):
    existing_user = await find_user_by_email(db, user_reg.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )

    await create_user(db, user_reg.email, user_reg.password)
    return {"message": "User registered successfully"}


@router.post("/login/", summary="Login and get JWT tokens", response_model=JwtResponse)
async def login_user(user_log: UserInfoRequest, db: AsyncSession = Depends(get_db)):
    existing_user = await find_user_by_email(db, user_log.email)
    if not existing_user or not existing_user.verify_password(user_log.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    payload = {"sub": str(existing_user.id), "email": existing_user.email}
    access_token = create_access_token(payload)
    refresh_token = create_refresh_token(payload)

    return JwtResponse(access_token=access_token, refresh_token=refresh_token)


@router.post(
    "/refresh/",
    summary="Refresh access token using refresh token",
    response_model=JwtAccessResponse,
)
async def refresh_access_token(
    payload: dict = Depends(verify_refresh_token), db: AsyncSession = Depends(get_db)
):
    existing_user = await find_user_by_email(db, payload.get("email"))
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    new_access_token = create_access_token(
        {"sub": str(existing_user.id), "email": existing_user.email}
    )

    return JwtAccessResponse(access_token=new_access_token)


@router.get(
    "/me/",
    summary="Get user information based on access token",
    response_model=UserInfoResponse,
)
async def get_user_info(
    payload: dict = Depends(verify_access_token), db: AsyncSession = Depends(get_db)
):
    existing_user = await find_user_by_email(db, payload.get("email"))
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
        )

    return UserInfoResponse(id=str(existing_user.id), email=existing_user.email)
