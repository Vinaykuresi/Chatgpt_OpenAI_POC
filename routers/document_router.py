from fastapi import Depends, APIRouter, UploadFile, File, HTTPException
from ..dependencies import get_openai_client
from ..services.document_service import process_document_logic
import docx
from io import BytesIO

router = APIRouter()

@router.post("/process-document")
async def process_document(file: UploadFile = File(...), openai_client=Depends(get_openai_client)):
    # Check if the uploaded file is a Word document
    if file.content_type != 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a Word document.")

    # Read the document
    try:
        file_bytes = await file.read()
        doc = docx.Document(BytesIO(file_bytes))
        full_text = [para.text for para in doc.paragraphs]
        document_content = '\n'.join(full_text)
        defined_text = process_document_logic(document_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # For now, just return the extracted text
    return {"content": defined_text}


