import os

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()
