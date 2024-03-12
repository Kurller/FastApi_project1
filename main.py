from fastapi import FastAPI
from fastapi import FastAPI,HTTPException,status,Depends
import psycopg2
#from app.database import engine,get_db
from router import scrape,user,Auth
app = FastAPI()

# Include the scrape router
app.include_router(scrape.router)
app.include_router(user.router)
app.include_router(Auth.router)