from pydantic import BaseModel


class UserInfoRequest(BaseModel):
    email: str
    password: str


class UserInfoResponse(BaseModel):
    id: str
    email: str


class JwtResponse(BaseModel):
    access_token: str
    refresh_token: str
    type: str = "Bearer"


class JwtAccessResponse(BaseModel):
    access_token: str
    type: str = "Bearer"
