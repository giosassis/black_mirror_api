from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routers import episodes_router, views_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(episodes_router.router)
app.include_router(views_router.router)

@app.get("/")
def read_root():
    print("Server is running")
    return {"message": "welcome to my personal application"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
