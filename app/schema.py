from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class user(BaseModel):
    username: Optional[str] = Field(
        None, title="Full Name Optional Args"
    )
    email: Optional[EmailStr] = Field(
        None, title="Email Optional Args"
    )
    password: str = Field(
        None, title="Password Optional Args"
    )
    confirmPassword: str = Field(
        None, title="Confirm Password Optional Args"
    )


class loginUser(user):
    email: EmailStr
    password: str = Field(min_length=12, max_length=100)


class signupUser(loginUser):
    username: str = Field(min_length=8, max_length=100)
    confirmPassword: str = Field(min_length=12, max_length=100)
