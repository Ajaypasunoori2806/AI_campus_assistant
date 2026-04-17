from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="AI Campus Assistant")   # <-- THIS LINE IS VERY IMPORTANT

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Server is running"}