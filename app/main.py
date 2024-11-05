from fastapi import FastAPI, HTTPException
from app.api.news import router as news_router

app = FastAPI()

# Include routers
app.include_router(news_router)
