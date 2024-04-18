from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings
sqlalchemy_database_url="postgresql://postgres:akhilesh@localhost/try"

engine=create_engine(sqlalchemy_database_url)
sesionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()    
def get_db():
    db = sesionlocal()
    try:
        yield db
    finally:
        db.close()     