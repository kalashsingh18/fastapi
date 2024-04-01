
# from fastapi import FastAPI,HTTPException,Response,status
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# import psycopg2
# from psycopg2.extras import RealDictCursor

# import random

# mypost=[{"title":"first","content":"first","id":1},{"title":"secound","content":"secound","id":2}]

# conector=psycopg2.connect(host='localhost',database='Fastapi',user='postgres',password='akhilesh',cursor_factory=RealDictCursor)

# conn=conector.cursor()
 




# app = FastAPI()
# class post(BaseModel):
#     title:str = None
#     content:str
#     published:bool =True
# @app.get("/")
# @app.get("/")
# def root():
#     try:
#         conn.execute("SELECT * FROM posts")
#         users = conn.fetchall()
#         print("Users:", users)  # Print query results for debugging
#         return {"roots": users}
#     except Exception as e:
#         print("Error:", e)
#         return {"error": "An error occurred while fetching data from the database"}



# @app.get("/posts")
# def root():
#     return {"root2": "called"}

# @app.post("/posts")
# def rooty_post(requ:post,Response:Response):
    
#     mydict=requ.dict()
#     mydict["id"]=random.randrange(0,1000)
#     mypost.append(mydict)
#     Response.status_code=status.HTTP_200_OK
#     status_code=Response.status_code
#     return {"rooty": mypost,"status":status_code}


# @app.get("/posts/{id}")
# def get_post(id):
#     print(id)
    
#     for i in mypost:
#         if i["id"]==int(id):
#             x=i
#             return {"id":x}
#     else:
#         return {"id":"doesnot exist"}
from fastapi import FastAPI,Depends
import psycopg2 
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

import models
from database import engine,sesionlocal,get_db
from sqlalchemy.orm import Session
get_db()
try:
    # Attempt to create all tables
    models.Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
except Exception as e:
    # Print the error message if an exception occurs
    print("Error occurred while creating tables:", e)

print("connected")

app=FastAPI()
# conn =psycopg2.connect(host='localhost',user='postgres',password='akhilesh',database="Fastapi",cursor_factory=RealDictCursor)
# cursor=conn.cursor()
class post(BaseModel):
    title:str
    about:str

# @app.get("/")
# def gets(post:post):
#     cursor.execute("SELECT * FROM posts")
#     post=cursor.fetchall()
#     print(post)
#     return {"user":post}
@app.get("/sql")
def gets(db: Session = Depends(get_db)):
    sucess=db.query(models.Post).all()
    return {"status": sucess}
# @app.get("/post/{id}")
# def gets(id: int):
    
#     cursor.execute("SELECT * FROM posts WHERE id =%s",(id,))
#     specific_post=cursor.fetchone()
#     return {"posts":specific_post}
# @app.post("/post")
# def post(post:post):
#     print(post.title,post.about,type(post))
#     cursor.execute("INSERT INTO posts (title,about) VALUES (%s,%s) returning * ",(post.title,post.about))
#     conn.commit()
#     data=cursor.fetchone()
#     return {"create":data}
# @app.delete("/post/{name}")
# def delete_post(name:int):
#     cursor.execute("delete from posts where id = %s returning * ",(str(name),))
#     deleted=cursor.fetchone()
#     conn.commit()
#     return {"delete": deleted}


            


