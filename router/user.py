from ..import models
from ..import schemas
@app.post("/user")
def create_User(post:schemas.user,db:Session=Depends(get_db)):
    new_user=models.User(email=post.email,name=post.name)
    db.add(new_user)
    
    db.commit()
    db.refresh(new_user)
    return new_user    
@app.get("/user")
def get_method(db:Session=Depends(get_db)):
    return {"data":db.query(models.User).all()}
@app.get("/user/{id}")
def get_id(id:int,db:Session=Depends(get_db)):
    print(id)
    print(db.query(models.User).filter(models.User.id==id).all())
    return {"data":db.query(models.User).filter(models.User.id==id).all()}

@app.delete("/user/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    post=db.query(models.User).filter(models.User.id==id)
    post.delete(synchronize_session=False)
    db.commit()

    return post
            