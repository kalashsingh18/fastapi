
from pydantic import BaseModel,EmailStr
class post(BaseModel):
    title:str
    content:str
    published:bool
    class Config:
        orm_mode=True
class user(BaseModel):
    email:EmailStr
    name: str
    password: str
class login_user(BaseModel):
    email:EmailStr
    password:str
    
    