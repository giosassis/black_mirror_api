from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, controllers

router = APIRouter()

@router.get("/episodes", response_model=list[schemas.Episode], status_code=200)
def get_episodes(db: Session = Depends(database.get_db)):
    return controllers.fetch_episodes(db)
