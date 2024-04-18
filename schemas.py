
from pydantic import BaseModel,EmailStr
from typing import Optional
class user_out(BaseModel):
    email:EmailStr
    name: str
class post(BaseModel):
    title:str
    content:str
    published:bool
class post_out(BaseModel):
    posts:post
    votes:int
class posts(BaseModel):
    title:str
    content:str
    published:bool
    owner:user_out
    owner_id:int

class user(BaseModel):
    email:EmailStr
    name: str
    password: str
class login_user(BaseModel):
    email:EmailStr
    password:str
class token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str]
    password:str
class votes(BaseModel):
    post_id: int 
    dir :int
    
    