# Service to log workouts and provide summaries
from typing import List, Dict
import sqlite3

DB_PATH = "workouts.sqlite3"

def log_workout(exercise_type: str, duration_minutes: float) -> None:
    """Store a workout in the sqlite database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY, type TEXT, duration REAL)")
    c.execute("INSERT INTO workouts (type, duration) VALUES (?, ?)", (exercise_type, duration_minutes))
    conn.commit()
    conn.close()

def get_daily_summary() -> str:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT type, SUM(duration) FROM workouts GROUP BY type")
    rows = c.fetchall()
    conn.close()
    if not rows:
        return "No workouts logged today."
    summary = ", ".join(f"{typ}: {duration:.0f} min" for typ, duration in rows)
    return f"Today's activities: {summary}"
