from fastapi import FastAPI
from routers import document_router, audio_router
from fastapi.responses import JSONResponse
from exceptions.custom_exceptions import AudioProcessingError, DocumentProcessingError, OpenAIRequestError, FileHandlingError

app = FastAPI()

@app.exception_handler(AudioProcessingError)
async def audio_processing_exception_handler(request, exc: AudioProcessingError):
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc)}
    )

@app.exception_handler(DocumentProcessingError)
async def document_processing_exception_handler(request, exc: DocumentProcessingError):
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc)}
    )

@app.exception_handler(OpenAIRequestError)
async def audio_processing_exception_handler(request, exc: OpenAIRequestError):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

@app.exception_handler(FileHandlingError)
async def document_processing_exception_handler(request, exc: FileHandlingError):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

app.include_router(document_router.router)
app.include_router(audio_router.router)
