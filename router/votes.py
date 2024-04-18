from fastapi import APIRouter,Depends
from database import get_db
import models
from .auth import get_current_user
from sqlalchemy.orm  import Session
from schemas import votes
router_votes=APIRouter()
@router_votes.post("/votes")
def votes(data:votes,db :Session =Depends(get_db),current_user: int =Depends(get_current_user)):
    if current_user:
      post=db.query(models.Post).filter(models.Post.id==data.post_id).first()
      ch=db.query(models.vote).filter(models.vote.post_id==data.post_id,models.vote.user_id==current_user.id)
      check=db.query(models.vote).filter(models.vote.post_id==data.post_id,models.vote.user_id==current_user.id).scalar()
      print(check,"cj")
      if data.dir==1 and post:
        
        
        if check:
            return {"message ": "already the vote exist"} 
        else:
            new_votes=models.vote(user_id=current_user.id,post_id=data.post_id)
            db.add(new_votes)
            db.commit()
            return {"message":"voted"}
      else:
          if not check:
              return {"message ": " the vote  does not exist"} 
          else:
              ch.delete(synchronize_session=False)
              db.commit()
              return {"message":"success fully deleted"}
    else:
        return {"message":"you are not authenicated"}
    