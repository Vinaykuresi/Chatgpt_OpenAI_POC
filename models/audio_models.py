from pydantic import BaseModel

class AudioRequest(BaseModel):
    filename: str

class AudioResponse(BaseModel):
    original_transcription: str
    corrected_transcription: str
