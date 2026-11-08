# Fitness Tracker Voice 01

A modular, production-grade starting point for a full-duplex, low-latency, voice-driven workout tracking application.

## Project Structure
- `src/` — Main application code and logic
- `config/` — Configuration files and technical specification
- `simulation_tests/` — Scripts to simulate and test app behavior
- `local_tools/` — Utilities, helper scripts, and local tooling

## Features
- Voice interaction with full-duplex, server-side VAD (350ms threshold)
- Two core intents: track workout (type and duration), and daily summary
- System prompt for energetic, punchy gym coach responses

## Getting Started

### 1. Install Python (3.8+ recommended)
Make sure Python is installed and available on your PATH.

### 2. (Optional) Create virtual environment
```shell
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies (if needed)
This starter has no external package requirements, but add them as you extend.

### 4. Run the simulation test
```shell
python simulation_tests/test_simulation.py
```
This script will:
- Simulate user utterances for both intents
- Show how the app parses and responds

### 5. Extending the App
- Add microphone/audio code to src/ as needed
- Implement real data storage for workouts
- Build out additional intents or response logic in `src/voice_fitness.py`
- Update the technical spec and prompt as your needs grow

## Governance
- All setup, file changes, and validation run through the audited, approval-based workflow. 
- Project is clean, modular, and production-grade from first commit!

---

**You’re ready to build, demo, and extend this voice-driven fitness tracking project!**
