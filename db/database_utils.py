from .models import User
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


async def find_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalar_one_or_none()
    return user


async def create_user(db: AsyncSession, email: str, password: str):
    user = User(email=email, password=password)
    db.add(user)
    await db.commit()
