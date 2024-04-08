from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash(password:str):
    print("executed")
    return pwd_context.hash(password)
def verify(plainpassword,storedpassword):
    return pwd_context.verify(plainpassword,storedpassword)