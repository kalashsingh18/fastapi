from database import Base
from sqlalchemy import Column,INTEGER,String,Boolean
from sqlalchemy.sql.expression import null
class Post(Base):
    __tablename__="post"
    id=Column(INTEGER,primary_key=True,nullable=False)
    content=Column(String,nullable=False)
    title=Column(String,nullable=False)
    published=Column(Boolean,nullable=False,default=True)