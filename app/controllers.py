from sqlalchemy.orm import Session
from . import services

def fetch_episodes(db: Session):
    return services.get_episodes(db)

def watch_episode(db: Session, episode_id: int):
    return services.mark_episode_as_watched(db, episode_id)