# Configuration for fitness-tracker-voice-01 backend

import os

class Settings:
    APP_NAME = "Fitness Tracker Voice 01"
    VAD_THRESHOLD_MS = 350
    ENABLE_FULL_DUPLEX = True
    LOGGING_LEVEL = "INFO"
    DB_PATH = os.getenv("WORKOUT_DB_PATH", "workouts.sqlite3")

settings = Settings()
