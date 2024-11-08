# app/schemas.py
from pydantic import BaseModel

class EpisodeBase(BaseModel):
    episode_id: int
    episode_name: str
    description: str
    season: int
    episode_number: int
    rating: float

class EpisodeCreate(EpisodeBase):
    pass

class Episode(EpisodeBase):
    episode_id: int

    class Config:
        orm_mode = True
