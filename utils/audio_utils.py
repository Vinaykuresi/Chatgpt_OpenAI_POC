from pydub import AudioSegment
from io import BytesIO
from exceptions.custom_exceptions import AudioProcessingError, FileHandlingError

def convert_audio_stream_to_wav(audio_stream):
    """
    Converts an audio stream to WAV format and returns the WAV stream.

    :param audio_stream: A file-like object containing the audio.
    :return: A BytesIO object containing the WAV audio.
    """
    try:
        audio = AudioSegment.from_file(audio_stream)
        wav_stream = BytesIO()
        audio.export(wav_stream, format="wav")
        wav_stream.seek(0)
        return wav_stream
    except Exception as e :
        raise AudioProcessingError(f"Error in transcribing audio file: {str(e)}")

def save_audio_to_wav(source_path, target_path):
    """
    Converts an audio file to WAV format.

    :param source_path: Path to the source audio file.
    :param target_path: Path to save the converted WAV file.
    """
    try:
        audio = AudioSegment.from_file(source_path)
        audio.export(target_path, format="wav")
    except Exception as e :
        raise FileHandlingError(f"Error in saving audio file: {str(e)}")

def get_audio_duration(file_path):
    """
    Returns the duration of the audio file in seconds.

    :param file_path: Path to the audio file.
    :return: Duration in seconds.
    """
    try:
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000.0
    except Exception as e :
        raise FileHandlingError(f"Error in calculating the length of audio file: {str(e)}")