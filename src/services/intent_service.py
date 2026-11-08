# Service for intent detection from recognized text
from typing import Dict

def parse_intent(text: str) -> Dict:
    # Production implementation goes here: NLP, rules, etc.
    if "how" in text and "doing" in text:
        return {"intent": "daily_summary", "parameters": {}}
    for activity in ["spin", "run", "walk", "yoga", "cycle", "gym"]:
        if activity in text and "min" in text:
            try:
                minutes = int(''.join([c for c in text if c.isdigit()]))
            except Exception:
                minutes = None
            return {"intent": "track_workout", "parameters": {"exercise_type": activity, "duration_minutes": minutes}}
    return {"intent": "unrecognized", "parameters": {}}
