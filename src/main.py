from fastapi import FastAPI
from src.api import speech, intent, workout

app = FastAPI(title="Fitness Tracker Voice 01 API")

app.include_router(speech.router)
app.include_router(intent.router)
app.include_router(workout.router)

@app.get("/")
def root():
    return {"message": "Fitness Tracker Voice API is live!"}
