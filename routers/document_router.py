from fastapi import APIRouter, UploadFile, File, HTTPException
from services.document_service import DocumentService
from utils.file_utils import read_word_document, read_text_file
from models.document_models import DocumentRequest, DocumentResponse

router = APIRouter()
document_service = DocumentService()

@router.post("/process-document")
async def process_document(file: UploadFile = File(...), task: str = "summarize"):
    # Check if the uploaded file is a Word document
    if file.content_type != 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a Word document.")

    # Read the document
    try:
        file_bytes = await file.read()
        document_content = read_word_document(file_bytes)
        model="gpt-3.5-turbo-instruct"
        processed_text = document_service.process_document_logic(document_content, model, task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"content": processed_text}


