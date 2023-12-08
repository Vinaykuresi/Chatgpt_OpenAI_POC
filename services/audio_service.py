import speech_recognition as sr
from io import BytesIO
from openai import OpenAI

def transcribe(openai_client, audio_file, model="whisper-1", prompt=""):
    """
    Transcribes audio to text using a speech-to-text service.
    
    :param audio_file: The audio file to transcribe.
    :param prompt: Optional prompt to guide the transcription service.
    :return: The transcribed text.
    """

    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # If audio_file is in bytes, you can use:
    with sr.AudioFile(BytesIO(audio_file)) as source:
        audio_data = recognizer.record(source)

    try:
        with open(audio_data, "rb") as audio_file:
            transcript = openai_client.audio.transcriptions.create(
                model=model, 
                file=audio_file
            )
        return transcript['text']
    except Exception as e:
        raise RuntimeError(f"Error in transcribing audio file: {str(e)}")


def generate_corrected_transcript(temperature, system_prompt, audio_file, openai_client):
    transcribed_text = transcribe(openai_client, audio_file, "whisper-1", prompt="")
    response = openai_client.Completion.create(
        model="gpt-4",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribed_text
            }
        ]
    )
    return response.choices[0].message.content



