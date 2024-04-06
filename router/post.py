
from sqlalchemy.orm import Session
from main  import models
from main import schemas
from fastapi import FastAPI,Depends,APIRouter
from database import engine,sesionlocal,get_db
router_post=APIRouter(tags=['posts'])
@router_post.get("/post")
def gets(response_model=schemas.post,db: Session = Depends(get_db)):
    sucess=db.query(models.Post).first()
    print(sucess)
    print(type(sucess))
    return sucess
@router_post.get("/post/{id}")
def get_by_id(id:int, post:schemas.post ,db: Session = Depends(get_db)):
    sucess=db.query(models.Post).filter(models.Post.id==id).all()
    print(sucess)
    print(post)
    return {"sucess":sucess}
@router_post.post("/post")
def post(posts:schemas.post,db : Session= Depends(get_db)):
    print(posts.title,posts.content)

   
    new_post=models.Post(**posts.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
  
    return {"post":new_post}
@router_post.delete("/posts/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
    post.delete(synchronize_session=False)
    db.commit()
    
    return {"post","deleted"}