from fastapi import FastAPI,HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from app import Schemas
from app.database import engine,get_db
from app import utils
from router import oAuth
from app import models,Schemas
router = APIRouter(tags = ['Authentication'])

@router.post("/login")
def login(user_credential: Schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.email).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = oAuth.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
