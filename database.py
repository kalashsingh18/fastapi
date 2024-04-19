from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings
sqlalchemy_database_url="postgres://fastapiuser:Axhcy8nhpba61kFaITHvhGAFbwScHJCS@dpg-coh27onsc6pc73aet7ug-a.oregon-postgres.render.com/fastapi_i3fn"

engine=create_engine(sqlalchemy_database_url)
sesionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()    
def get_db():
    db = sesionlocal()
    try:
        yield db
    finally:
        db.close()     