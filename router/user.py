from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import FastAPI,HTTPException,status,Depends,APIRouter
from app import models,Schemas
from app.models import User as DBScrape1  # Renaming the model class to avoid conflict
from app.database import get_db
from router import oAuth
from pydantic import BaseModel
from app import utils

router = APIRouter(prefix ="/users",tags =['User'])


@router.post('/',status_code=status.HTTP_201_CREATED,response_model= Schemas.UserOut)
def create_User(user:Schemas.UserCreate,db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/",response_model=list[Schemas.UserOut])
def get_users(db: Session = Depends(get_db),user_id: int = Depends(oAuth.get_current_user)):
    users = db.query(models.User).all()
    return users
@router.get("/{id}",response_model=Schemas.UserOut)
def get_user(id:int,db: Session = Depends(get_db)):
    user =  db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return user
@router.put("/{id}")
def update_user(id: int,updated_user:Schemas.UserUpdate,db: Session = Depends(get_db),user_id: int = Depends(oAuth.get_current_user)):
    user_update= db.query(models.User).filter(models.User.id == id).first()
    if user_update == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    for key, value in updated_user.dict().items():
            setattr(user_update, key, value)
    db.commit()
    return {"message": "Data updated successfully", "updated_data": updated_user.dict()}
@router.delete("/{id}")
def delete_user(id:int,db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(user)
    db.commit()
    return {"user successfully deleted" }