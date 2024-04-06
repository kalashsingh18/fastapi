from main import models
from main import schemas
from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session

router_user=APIRouter(tags=['user'])
@router_user.post("/login")
def create_User(post:schemas.user,db:Session=Depends(get_db)):
    new_user=models.User(email=post.email,name=post.name)
    db.add(new_user)
    
    db.commit()
    db.refresh(new_user)
    return new_user    
@router_user.get("/login")
def get_method(db:Session=Depends(get_db)):
    return {"data":db.query(models.User).all()}
@router_user.get("/login/{id}")
def get_id(id:int,db:Session=Depends(get_db)):
   
    return {"data":db.query(models.User).filter(models.User.id==id).all()}

@router_user.delete("/login/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    post=db.query(models.User).filter(models.User.id==id)
    post.delete(synchronize_session=False)
    db.commit()

    return post