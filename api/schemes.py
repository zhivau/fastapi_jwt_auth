from pydantic import BaseModel, EmailStr


class UserInfoRequest(BaseModel):
    email: EmailStr
    password: str


class UserInfoResponse(BaseModel):
    id: str
    email: EmailStr


class JwtResponse(BaseModel):
    access_token: str
    refresh_token: str
    type: str = "Bearer"


class JwtAccessResponse(BaseModel):
    access_token: str
    type: str = "Bearer"
