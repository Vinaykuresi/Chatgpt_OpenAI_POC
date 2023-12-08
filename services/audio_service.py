import speech_recognition as sr
from io import BytesIO
from .openai_service import OpenAIService
from exceptions.custom_exceptions import AudioProcessingError, OpenAIRequestError

class AudioService:
    def __init__(self):
        self.openai_service = OpenAIService()

    def transcribe(self, audio_file, model="whisper-1", prompt=""):
        """
        Transcribes audio to text using a speech-to-text service.
        
        :param audio_file: The audio file to transcribe.
        :param prompt: Optional prompt to guide the transcription service.
        :return: The transcribed text.
        """
        try:
            # Initialize the speech recognizer
            recognizer = sr.Recognizer()

            # If audio_file is in bytes, you can use:
            with sr.AudioFile(BytesIO(audio_file)) as source:
                audio_data = recognizer.record(source)
                response = self.openai_service.transcribe_audio(audio_data, model)
        except Exception as e:
            raise AudioProcessingError(f"Failed to process transcription: {str(e)}")
        
        return response


    def generate_corrected_transcript(self, temperature, system_prompt, audio_file):
        try:
            transcribed_text = self.transcribe(audio_file, "whisper-1", prompt="")
            response  = self.openai_service.corrected_audio(temperature, system_prompt, transcribed_text, model="gpt-4")
        except Exception as e:
            raise OpenAIRequestError(f"Error in transcribing audio file: {str(e)}")
        
        return response



