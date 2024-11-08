from sqlalchemy.orm import Session
from . import models, schemas

def get_episodes(db: Session):
    return db.query(models.Episode).order_by(models.Episode.rating.desc()).all()

def mark_episode_as_watched(db: Session, episode_id: int):
    episode = db.query(models.Episode).filter(models.Episode.episode_id == episode_id).first()
    if episode:
        episode.watched = True
        db.commit()
        db.refresh(episode)
    return episode