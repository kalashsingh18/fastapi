from main import models
from main import schemas
from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
from .import utils

router_user=APIRouter(tags=['user'])
@router_user.post("/user")
def create_User(post:schemas.user,db:Session=Depends(get_db)):
    
    newpassword=utils.hash(post.password)
    post.password=newpassword
    
    
   
    
    
    
    
    new_user=models.User(email=post.email,name=post.name,password=post.password)
    db.add(new_user)
    
    db.commit()
    db.refresh(new_user)
    x="p"
    return new_user
@router_user.get("/user")
def get_method(db:Session=Depends(get_db)):
    return {"data":db.query(models.User).all()}
@router_user.get("/user/{id}")
def get_id(id:int,db:Session=Depends(get_db)):
   
    return {"data":db.query(models.User).filter(models.User.id==id).all()}

@router_user.delete("/user/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    post=db.query(models.User).filter(models.User.id==id)
    post.delete(synchronize_session=False)
    db.commit()

    return post