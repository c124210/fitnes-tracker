# Pydantic schemas for API requests and responses

from pydantic import BaseModel
from typing import Optional, List

class RecognizeSpeechRequest(BaseModel):
    audio_data: bytes
    sample_rate: int
    channels: int
    vad: Optional[bool] = True

class RecognizeSpeechResponse(BaseModel):
    recognized_text: str

class SynthesizeSpeechRequest(BaseModel):
    text: str

class SynthesizeSpeechResponse(BaseModel):
    audio_data: bytes
    sample_rate: int
    channels: int

class WorkoutLogRequest(BaseModel):
    exercise_type: str
    duration_minutes: float

class WorkoutLogResponse(BaseModel):
    success: bool
    message: str

class DailySummaryResponse(BaseModel):
    summary: str

class IntentParseRequest(BaseModel):
    text: str

class IntentParseResponse(BaseModel):
    intent: str
    parameters: dict
