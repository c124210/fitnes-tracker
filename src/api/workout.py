from fastapi import APIRouter
from src.services.workout_service import log_workout, get_daily_summary
from src.models.schemas import WorkoutLogRequest, WorkoutLogResponse, DailySummaryResponse

router = APIRouter()

@router.post("/workout/log", response_model=WorkoutLogResponse)
def log(req: WorkoutLogRequest):
    try:
        log_workout(req.exercise_type, req.duration_minutes)
        return WorkoutLogResponse(success=True, message="Workout logged successfully.")
    except Exception as e:
        return WorkoutLogResponse(success=False, message=f"Error: {e}")

@router.get("/summary/daily", response_model=DailySummaryResponse)
def get_daily():
    summary = get_daily_summary()
    return DailySummaryResponse(summary=summary)
