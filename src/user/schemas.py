import re
from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


def _validate_bcrypt_password_length(value: str) -> str:
    if len(value.encode("utf-8")) > 72:
        raise ValueError("Password must be at most 72 UTF-8 bytes for bcrypt")
    return value


class UserType(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"


class User(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    user_type: UserType
    password: str = Field(
        min_length=8,
        description="At least 8 characters, including uppercase, lowercase, a number, and a special character",
        examples=["SecurePassword123!"],
    )
    birthdate: date = Field(
        description="Date format: YYYY-MM-DD",
        examples=["1998-05-21"],
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\/~`;'']", value):
            raise ValueError("Password must contain at least one special character")
        if re.search(r"\s", value):
            raise ValueError("Password must not contain spaces")

        return _validate_bcrypt_password_length(value)


class Login(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, value: str) -> str:
        return _validate_bcrypt_password_length(value)


class ShowUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    birthdate: date
    username: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None


class UserInDB(BaseModel):
    email: EmailStr
    hashed_password: str