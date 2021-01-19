from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr, Field
from pydantic.utils import almost_equal_floats
from sqlalchemy.orm import Session
from app.db import get_db
from app.model import User_list


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


async def authLogin(user: loginUser):
    # if db["email"] != user.email:
    #     return False
    # else:
    #     if db['password'] != user.password:
    #         return False
    #     else:
    return True


def findByEmail(email: EmailStr, db: Session):
    return db.query(User_list).filter(User_list.email == email).count()


def findByusername(username: str, db: Session):
    return db.query(User_list).filter(User_list.username == username).count()


def confirmPasswordCheck(password: str, confirmPassword: str):
    if(password != confirmPassword):
        return 0
    else:
        return 1


app = FastAPI()


@app.post("/signup", status_code=status.HTTP_201_CREATED)
def createUser(user: signupUser, db: Session = Depends(get_db)):
    if(findByEmail(user.email, db)):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Email already taken")

    if(findByusername(user.username, db)):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Username already taken")
    if(confirmPasswordCheck(user.password, user.confirmPassword) == 0):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="confirm Password doesnot match with Password")
    to_create = User_list(
        email=user.email,
        username=user.username,
        password=user.password
    )
    db.add(to_create)
    db.commit()
    return {"success": "ok"}


@app.post("/login")
async def loginUser(user: loginUser):
    if(await authLogin(user)):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
