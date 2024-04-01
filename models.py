from database import Base
from sqlalchemy import Column,INTEGER,String,Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__="post"
    id=Column(INTEGER,primary_key=True,nullable=False)
    content=Column(String,nullable=False)
    title=Column(String,nullable=False)
    published=Column(Boolean,nullable=False,server_default='True')
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))