"""Core module for full-duplex voice-driven workout tracking and daily summary."""

from typing import List, Dict, Any

def track_workout(exercise_type: str, duration_minutes: float) -> Dict[str, Any]:
    """Log a workout by type and duration."""
    # Placeholder actual implementation: append record, integrate with durable store
    return {
        "event": "workout_tracked",
        "type": exercise_type,
        "duration": duration_minutes
    }

def daily_summary() -> Dict[str, Any]:
    """Return a summary of today’s workouts (mock)."""
    # Placeholder: In a real app, aggregate from real workout data store
    return {
        "event": "daily_summary",
        "summary": "3 activities: 45 min cycling, 20 min strength, 30 min yoga"
    }

def parse_intent(user_utterance: str) -> Dict[str, Any]:
    """Parse intent and parameters from informal utterance (mock only)."""
    utterance = user_utterance.lower()
    if "how am i doing" in utterance or "summary" in utterance:
        return daily_summary()
    # Naive extraction: look for activity with duration
    if "min" in utterance:
        for kw in ["spin", "run", "walk", "yoga", "cycle", "gym"]:
            if kw in utterance:
                words = utterance.split()
                for token in words:
                    if token.endswith("min"):
                        try:
                            minutes = float(token.replace("min", ""))
                            return track_workout(kw, minutes)
                        except Exception:
                            continue
    return {"event": "unrecognized", "input": user_utterance}
