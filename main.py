from fastapi import FastAPI
from routers import document_router, audio_router

app = FastAPI()

app.include_router(document_router.router)
app.include_router(audio_router.router)
