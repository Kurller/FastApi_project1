from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from app.database import Base, engine
class Scrape(Base):
    __tablename__ = 'scrape'
    id = Column(Integer, primary_key=True)
    companyNames = Column(String, nullable=False)
    job_titles = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="scrapes")
    location = Column(String)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    scrapes = relationship("Scrape", back_populates="user")
    phone_number = Column(String)

#Base.metadata.create_all(engine)
