from pydantic_settings import BaseSettings

class Settings(BaseSettings):
      data_base_password:str
      SECRET_KEY:str
      ALGORITHM:str
      ACCESS_TOKEN_EXPIRE_MINUTES:str
      
      
      class config:
          env_file=".env"
