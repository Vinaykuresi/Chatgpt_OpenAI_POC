from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from ..dependencies import get_openai_client
from ..services.audio_service import generate_corrected_transcript

router = APIRouter()

@router.post("/process-audio")
async def process_audio(file: UploadFile = File(...), openai_client=Depends(get_openai_client)):

    # Check if the uploaded file is an audio file
    if not file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an audio file.")
    
    try:
        # optional for better prompting
        system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."
        corrected_text = generate_corrected_transcript(0, system_prompt, file.file, openai_client)
        return {"corrected_transcription": corrected_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio file: {str(e)}")