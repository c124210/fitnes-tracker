from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.speech_service import recognize_speech, synthesize_speech
from src.models.schemas import RecognizeSpeechRequest, RecognizeSpeechResponse, SynthesizeSpeechRequest, SynthesizeSpeechResponse

router = APIRouter()

@router.post("/speech/recognize", response_model=RecognizeSpeechResponse)
def recognize(req: RecognizeSpeechRequest):
    # Call your voice recognition service
    text = recognize_speech(req.audio_data, req.sample_rate, req.channels, vad=req.vad or True)
    return RecognizeSpeechResponse(recognized_text=text)

@router.post("/speech/synthesize", response_model=SynthesizeSpeechResponse)
def synthesize(req: SynthesizeSpeechRequest):
    audio, sample_rate, channels = synthesize_speech(req.text)
    return SynthesizeSpeechResponse(audio_data=audio, sample_rate=sample_rate, channels=channels)
