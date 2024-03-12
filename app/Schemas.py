from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
class UserCreate(BaseModel):
    email:EmailStr
    password:str
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    #owner_id:int
class UserLogin(BaseModel):
    email:EmailStr
    password:str
class UserUpdate(UserCreate):
    pass
class UserLogin(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str] = None

    
    
    class config:
        orm_mode =True