from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.crud import findByEmail, findByusername
from app.auth import NotConfirmPassword
from app.db import get_db
from app.crud import create_user
from app.schema import LoginUser, SignupUser


app = FastAPI()


@app.post("/signup", status_code=status.HTTP_201_CREATED)
def create_User(user: SignupUser, db: Session = Depends(get_db)):
    if(findByEmail(user.email, db) != None):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Email already taken")
    if(findByusername(user.username, db) != None):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Username already taken")
    if(NotConfirmPassword(user.password, user.confirmPassword)):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="confirm Password doesnot match with Password")
    dbuser = create_user(db, user)
    return {
        "success": "OK",
        "user": dbuser}  # Testing er jono I have to remove this


@app.post("/login")
async def login_User(user: LoginUser, db: Session = Depends(get_db)):

    # else:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
