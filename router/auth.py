from fastapi import Depends,APIRouter,HTTPException
from main import models
from main import schemas
from database import get_db
from router import utils
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
import dificult
router_auth=APIRouter(tags=["auth"])
from jose import jwt
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
print("heree")
@router_auth.post("/login")

# Assuming these constants are defined somewhere in your code


def login_auth(user_credatilas: schemas.login_user, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credatilas.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if utils.verify(user_credatilas.password, user.password):
        access_token = create_access_token(data={"user_id": user.id})
        return access_token
    else:
        raise HTTPException(status_code=401, detail="Incorrect password")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt