
from pydantic import BaseModel,EmailStr
class post(BaseModel):
    title:str
    content:str
    published:bool
    class Config:
        orm_mode=True
class user(BaseModel):
    name: str
    email:EmailStr
    
    