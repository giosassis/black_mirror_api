from fastapi import APIRouter, Depends, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import controllers, database 
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/ranking", response_class=HTMLResponse)
async def ranking(request: Request, db: Session = Depends(database.get_db)):
    episodes = controllers.fetch_episodes(db)
    return templates.TemplateResponse("table_template.html", {"request": request, "episodes": episodes})
