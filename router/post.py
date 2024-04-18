
from sqlalchemy.orm import Session
from main  import models
from typing import List,Optional
from .import auth
import models
from main import schemas
from sqlalchemy import func


from fastapi import FastAPI,Depends,APIRouter
from database import engine,sesionlocal,get_db
router_post=APIRouter(tags=['posts'])
@router_post.get("/post", response_model=List[schemas.post_out])
def get_posts(db: Session = Depends(auth.get_db),
              current_user=Depends(auth.get_current_user),

              search: Optional[str] = ""):
    if current_user is not None:
        print(current_user.id)
        posts = db.query(models.Post).all() 
        print(posts)
        response = []
        for post in posts:
            
            

# Perform the query
            vote_count = db.query(func.count(models.vote.post_id)) \
                           .filter(models.vote.post_id == post.id) \
                           .scalar()
            post_out = schemas.post_out(posts=post.__dict__, votes=vote_count)
            
            response.append(post_out)
        
        
        return response
@router_post.get("/post/{id}")
def get_by_id(id:int ,db: Session = Depends(get_db), current_user: int = Depends(auth.get_current_user)):
    if current_user is not  None:
       sucess=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
       return {"sucess":sucess}
    else:
        return {"mesage":"not authorized"}  

@router_post.post("/post")
def post(posts: schemas.post, db: Session = Depends(get_db), current_user:int = Depends(auth.get_current_user)):
    if current_user is not  None:
     
     current_user=current_user.id
     print("current_user",current_user)
     new_post = models.Post(owner_id=current_user,**posts.dict())
     email=db.query(models.User).filter(models.User.id==current_user).first()
     email=email.email
     
     db.add(new_post)
     db.commit()
     db.refresh(new_post)
     return {"post": new_post,"mail of  the user which created this , is ":email}
    else:
        return {"mesage":"not authorized"}
@router_post.delete("/post/{id}")
def delete(id:int,db:Session=Depends(get_db),current_user:int=Depends(auth.get_current_user)):
    if current_user is not  None:
        
        post=db.query(models.Post).filter(models.Post.id==id)
        posts=post.first()
        print("d",current_user.id)
        if posts.owner_id==current_user.id:
         post.delete(synchronize_session=False)
         db.commit()
         return {"post","deleted"}
        else:
            return {"message":"not authenicated to delete"}    
        
    else:
        return {"mesage":"not authorized"}
@router_post.put("/post/{id}")
def update(id:int,data:schemas.post,db:Session=Depends(get_db),curent_user:int=Depends(auth.get_current_user)):
    if curent_user is not None:
        
        p_t_update=db.query(models.Post).filter(models.Post.id==id).first()
        print("pt",p_t_update)
        if p_t_update.owner_id!=curent_user.id:
            return {"message":"not authorized to delete"}
        p_t_update.title=data.content
        p_t_update.content=data.title
        p_t_update.owner_id=curent_user.id
        
        db.commit()
        db.refresh(p_t_update)
        return {"updated":p_t_update}
        


    
    
    


    