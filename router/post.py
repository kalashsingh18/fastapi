
from sqlalchemy.orm import Session
from main  import models
from main import schemas
from fastapi import FastAPI,Depends,APIRouter
from database import engine,sesionlocal,get_db
router=APIRouter(tags=['posts'])
@router.get("/post")
def gets(response_model=schemas.post,db: Session = Depends(get_db)):
    sucess=db.query(models.Post).first()
    print(sucess)
    print(type(sucess))
    return sucess
@router.get("/post/{id}")
def get_by_id(id:int, post:schemas.post ,db: Session = Depends(get_db)):
    sucess=db.query(models.Post).filter(models.Post.id==id).all()
    print(sucess)
    print(post)
    return {"sucess":sucess}
@router.post("/posts")
def post(posts:schemas.post,db : Session= Depends(get_db)):
    print(posts.title,posts.content)

   
    new_post=models.Post(**posts.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
  
    return {"post":new_post}