from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import datetime
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expiration_minutes: int = 15):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=expiration_minutes
    )

    token = jwt.encode(
        {"exp": expiration_time, "iat": datetime.datetime.utcnow(), **data},
        settings.ACCESS_SECRET_KEY,
        algorithm="HS256",
    )
    return token


def verify_access_token(token: str = Depends(oauth2_scheme)):
    try:
        decoded = jwt.decode(token, settings.ACCESS_SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


def create_refresh_token(data: dict, expiration_days: int = 7):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(
        days=expiration_days
    )
    refresh_token = jwt.encode(
        {"exp": expiration_time, "iat": datetime.datetime.utcnow(), **data},
        settings.REFRESH_SECRET_KEY,
        algorithm="HS256",
    )
    return refresh_token


def verify_refresh_token(token: str = Depends(oauth2_scheme)):
    try:
        decoded = jwt.decode(token, settings.REFRESH_SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
