from main import models
from main import schemas
from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
from .import utils

from .auth import create_access_token,get_current_user

router_user=APIRouter(tags=['login'])
@router_user.post("/create_user")
def create_User(post:schemas.user,db:Session=Depends(get_db)):
  if not db.query(models.User).filter(models.User.email==post.email).first():
    newpassword=utils.hash(post.password)
    post.password=newpassword
    new_user=models.User(email=post.email,name=post.name,password=post.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":new_user.id,"id":new_user.id,"token":create_access_token(data={"user_id":new_user.id})}
  else:
      return {"mesaage":"the email already used "}
    
@router_user.get("/user")
def get_method(db:Session=Depends(get_db)):
    return {"data":db.query(models.User).all()}
@router_user.get("/user/{id}")
def get_id(id:int,db:Session=Depends(get_db)):
    return {"data":db.query(models.User).filter(models.User.id==id).all()}
   
@router_user.delete("/user/{id}")  
def delete(id:int,db:Session=Depends(get_db),current_user:int =Depends(get_current_user)):
    users=db.query(models.User).filter(models.User.id==current_user.id)
    user=users.first()
    users.delete(synchronize_session=False)
    db.commit()
    return users

