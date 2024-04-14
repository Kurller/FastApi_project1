from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import Scrape as DBScrape
from app.database import get_db
from router import oAuth
from pydantic import BaseModel
from typing import Optional
from app import models
from app.models import User,Scrape
from sqlalchemy import func

router = APIRouter(prefix="/get_data", tags=['Scraped-Data'])

class ScrapeBase(BaseModel):
    companyNames: str
    job_titles: str
    location:str

class ScrapeCreate(ScrapeBase):
    pass

@router.get("/")
def test_post(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    test_data = db.query(DBScrape).filter(DBScrape.companyNames.contains(search)).limit(limit).offset(skip).all()
    result = db.query(models.User.id, models.User.email, func.count(models.Scrape.id).label('scrape_count')) \
                    .outerjoin(models.Scrape, models.User.id == models.Scrape.user_id) \
                    .group_by(models.User.id, models.User.email).filter(DBScrape.companyNames.contains(search)).limit(limit).offset(skip).all() 
                    

        # Convert the query result into a list of dictionaries
    serialized_result = []
    for user_id, email, scrape_count in result:
            serialized_result.append({
                'user_id': user_id,
                'email': email,
                'scrape_count': scrape_count
            })

    #return serialized_result
    return {"status": test_data}

@router.get("/{id}")
def get_scrape(id: int, db: Session = Depends(get_db), user_id: int = Depends(oAuth.get_current_user)):
    new_data = db.query(DBScrape).filter(DBScrape.id == id).first()
    return new_data

@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oAuth.get_current_user)):
    post = db.query(DBScrape).filter(DBScrape.id == id)
    
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    post.delete(synchronize_session=False)
    db.commit()

@router.put("/{id}")
def update_data(id: int, updated_data: ScrapeCreate, db: Session = Depends(get_db), user_id: int = Depends(oAuth.get_current_user)):
    data = db.query(DBScrape).filter(DBScrape.id == id).first()
    
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
    
    for key, value in updated_data.dict().items():
        setattr(data, key, value)
    
    db.commit()
    
    return {"message": "Data updated successfully", "updated_data": updated_data.dict()}

@router.post("/")
def create_post(data: ScrapeCreate, db: Session = Depends(get_db)):
    #user_id: int = Depends(oAuth.get_current_user))
    created_post = DBScrape(**data.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return {"data": created_post}
