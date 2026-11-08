"""Simulate and test voice fitness app's intents through mocked utterances."""
from src.voice_fitness import parse_intent

examples = [
    "Did a 30-minute spin today!",
    "How am I doing this week?",
    "Just finished a 25min run",
    "What's my daily summary?",
    "Did a 60min yoga session"
]

for utterance in examples:
    result = parse_intent(utterance)
    print(f"User: {utterance}\nAssistant (parsed): {result}\n")
