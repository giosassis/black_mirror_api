# delete_table.py
import sys
import os
from sqlalchemy import create_engine
from app.models import Episode
from app.database import Base

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

engine = create_engine("sqlite:///black_mirror.db")

Episode.__table__.drop(engine)

print("table successfully deleted")
