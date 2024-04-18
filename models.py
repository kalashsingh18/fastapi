from database import Base
from sqlalchemy import Column,INTEGER,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "User"
    id = Column(INTEGER, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    password = Column(String, nullable=False)
    phone_number=Column(String)


class Post(Base):
    __tablename__="post"
    id=Column(INTEGER,primary_key=True,nullable=False)
    content=Column(String,nullable=False)
    title=Column(String,nullable=False)
    published=Column(Boolean,nullable=False,server_default='True')
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    owner_id=Column(INTEGER,ForeignKey("User.id",ondelete="CASCADE"),nullable=False)
    owner=relationship(User)
class vote(Base):
   __tablename__="votes"
   post_id=Column(INTEGER,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)
   user_id=Column(INTEGER,ForeignKey("User.id",ondelete="CASCADE"),primary_key=True)
