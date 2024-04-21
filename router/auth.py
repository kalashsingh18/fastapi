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
def verify_access_token(tokens: str, credentials_exception: HTTPException):
 
        print("Token:", tokens)
        print(type(tokens))
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMSwiZXhwIjoyMDczNzMwNjYzfQ.Ng9vi_fq7O2x6qLm8_-wludc3FOmXJEp46TkLRias-0"
        print(token==tokens)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Payload:", payload)
        id = payload.get("user_id")
        print(id)
        print("User ID from token:",id)
    
        if id is None:
            print("User ID not found in token payload.")
            raise credentials_exception
        return id
        





def get_current_user(token: str = Depends(oauth2_scheme),db:Session =Depends(database.get_db)):
    global checks
    checks=token
    print("CHECK",checks,"token",token)
    credentials_exception = HTTPException(status_code=401, detail="Invalid token")
    tokens=verify_access_token(checks, credentials_exception)
    user=db.query(models.User).filter(models.User.id == tokens).first()
   
    return user   
    

  

  
     
  
    
