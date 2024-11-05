from fastapi import FastAPI, HTTPException
from app.api.news import router as news_router

app = FastAPI()

# Include routers
app.include_router(news_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the News Analysis API"}
