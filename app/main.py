from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session, Query
from app.hashpassword import verify_password, get_password_hash
from app.crud import findByEmail, findByusername
from app.db import get_db
from app.model import User_list
from app.schema import loginUser, signupUser


async def authLogin(user: loginUser, db: Session):
    userDb: Query = findByEmail(user.email, db)
    if userDb.count():
        verify_password(user.password, )


def confirmPasswordCheck(password: str, confirmPassword: str):
    if(password != confirmPassword):
        return 0
    else:
        return 1


app = FastAPI()


@app.post("/signup", status_code=status.HTTP_201_CREATED)
def createUser(user: signupUser, db: Session = Depends(get_db)):
    emailDb: Query = findByEmail(user.email, db)
    if(emailDb.count()):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Email already taken")
    usenameDb: Query = findByusername(user.username, db)
    if(usenameDb.count()):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Username already taken")
    if(confirmPasswordCheck(user.password, user.confirmPassword) == 0):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="confirm Password doesnot match with Password")
    hashPassowrd = get_password_hash(user.password)

    to_create = User_list(
        email=user.email,
        username=user.username,
        password=hashPassowrd
    )
    db.add(to_create)
    db.commit()
    return {"success": "ok"}


@app.post("/login")
async def loginUser(user: loginUser, db: Session = Depends(get_db)):

    # else:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
