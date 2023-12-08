from fastapi import APIRouter, UploadFile, File, HTTPException
from io import BytesIO
from services.audio_service import AudioService
from utils.audio_utils import convert_audio_stream_to_wav
from models.audio_models import AudioRequest, AudioResponse

router = APIRouter()
audio_service = AudioService()

@router.post("/process-audio")
async def process_audio(request: AudioRequest, file: UploadFile = File(...)):

    # Check if the uploaded file is an audio file
    if not file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an audio file.")
    
    try:
        # optional for better prompting
        system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

       # Read the file into memory
        file_bytes = await file.read()
        audio_stream = BytesIO(file_bytes)

        # Convert to WAV format
        wav_stream = convert_audio_stream_to_wav(audio_stream)

        corrected_text = audio_service.generate_corrected_transcript(0, system_prompt, wav_stream)
        return AudioResponse(corrected_transcription=corrected_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio file: {str(e)}")
    