from fastapi import APIRouter
from src.services.intent_service import parse_intent
from src.models.schemas import IntentParseRequest, IntentParseResponse

router = APIRouter()

@router.post("/intent/parse", response_model=IntentParseResponse)
def parse(req: IntentParseRequest):
    result = parse_intent(req.text)
    return IntentParseResponse(intent=result["intent"], parameters=result["parameters"])
