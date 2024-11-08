from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Episode(Base):
    __tablename__ = "episodes"

    episode_id = Column(Integer, primary_key=True, index=True)
    episode_name = Column(String, index=True)
    description = Column(String)
    season = Column(Integer)
    episode_number = Column(Integer)
    rating = Column(Float)