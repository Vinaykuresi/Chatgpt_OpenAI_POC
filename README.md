# FastAPI OpenAI Integration Project

## Introduction
This project is a FastAPI application that integrates OpenAI's Whisper model for audio transcription, GPT-4 for post-processing the transcribed text, and functionality to read and process text files. It allows users to upload audio and text files, transcribes audio files, and processes the content for various tasks like correcting spelling discrepancies or formatting.

## Features
- Audio file uploading and processing.
- Transcription of audio using OpenAI's Whisper model.
- Post-processing of transcribed text using GPT-4.
- Uploading and processing text files.

## Setup and Installation
To set up this project, follow these steps:

1. **Clone the Repository**
```python
    git clone https://github.com/Vinaykuresi/Chatgpt_OpenAI_POC
    cd Chatgpt_OpenAI_POC
```

2. **Create a Virtual Environment (Optional)**
```python
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. **Install Dependencies**
```python
pip install -r requirements.txt
```

4. **Environment Variables**
Set your OpenAI API key in your environment:
```python
export OPENAI_API_KEY='your-api-key'
```

## Usage
To run the FastAPI server:
```python
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### Endpoints
- `POST /process-audio/`: Upload an audio file for transcription.
- `POST /process-document/`: Upload a document for processing (if applicable).

## Testing
Need to be implemented

## Contribution
Vinay Kumar Kuresi

