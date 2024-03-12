from pydantic import BaseSettings



class Settings(BaseSettings):
    database_password:str
    database_hostname:str
    database_username:str
    database_name:str
    Algorithm:str
    Access_Token_expire_minutes:int
    secret_key:str
    
    class Config():
        env_file=".env"
settings=Settings()