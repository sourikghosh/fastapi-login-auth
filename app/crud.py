from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.model import User_list


def findByEmail(email: EmailStr, db: Session):
    return db.query(User_list).filter(User_list.email == email).first()


def findByusername(username: str, db: Session):
    return db.query(User_list).filter(User_list.username == username).first()
