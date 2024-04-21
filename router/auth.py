from fastapi import Depends,APIRouter,HTTPException
from fastapi.security import OAuth2PasswordBearer
from main import models
import database
from main import schemas
from database import get_db
from router import utils
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import jwt,JWTError


router_auth=APIRouter(tags=["auth"])

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 6000000
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

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
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# def verify_access_token(token: str, credentials_exception: HTTPException):
def verify_access_token(token: str, credentials_exception: HTTPException):
    try:
        
        print("token",token)

        
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        id = payload.get("user_id")
        print(id)
        if id is None:
            print("is is none",id)
            raise credentials_exception
        return id
    except jwt.ExpiredSignatureError:
     print("Token has expired")

    except JWTError:
        raise credentials_exception
def get_current_user(token: str = Depends(oauth2_scheme),db:Session =Depends(database.get_db)):
    check=token
    print("CHECK",check,"token",token)
    credentials_exception = HTTPException(status_code=401, detail="Invalid token")
    tokens=verify_access_token(check, credentials_exception)
    user=db.query(models.User).filter(models.User.id == tokens).first()
   
    return user   
    

  

  
     
  
    
