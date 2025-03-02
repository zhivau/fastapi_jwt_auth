from sqlalchemy import Column, Integer, String
from .database import Base
import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __init__(self, email, password):
        salt = bcrypt.gensalt()
        self.email = email
        self.hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt).decode(
            "utf-8"
        )

    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode("utf-8"), self.hashed_password.encode("utf-8")
        )
