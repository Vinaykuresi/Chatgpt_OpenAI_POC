from config import settings
import openai

def get_openai_client():
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set in the environment variables.")
    
    return openai.Client(api_key=settings.OPENAI_API_KEY)
