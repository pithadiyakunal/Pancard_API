from fastapi import FastAPI
import src.db.models
from src.config.config import engine
import src.urls.user

src.db.models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(src.urls.user.router)