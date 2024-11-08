import sys
import os
import pandas as pd
from sqlalchemy import create_engine
from app.database import SessionLocal
from app.models import Episode

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

file_path = os.path.join(os.path.dirname(__file__), 'episodes_dataset.csv')

df = pd.read_csv(file_path)

engine = create_engine("sqlite:///black_mirror.db")

df.to_sql("episodes", con=engine, if_exists="replace", index=False)

def load_data_to_db(df):
    db = SessionLocal()  
    try:
        for index, row in df.iterrows():
            episode = Episode(
                episode_name=row['episode_name'],   
                season=row['season'],
                episode_number=row['episode'],  
                rating=row['rating'],  
            )
            db.add(episode)
        db.commit()
    except Exception as e:
        print(f"there was an error when trying to insert data: {e}")
    finally:
        db.close()

# Carrega os dados no banco
load_data_to_db(df)

print("data was successfully imported!")
