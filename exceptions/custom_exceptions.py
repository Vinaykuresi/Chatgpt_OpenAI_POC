class AudioProcessingError(Exception):
    """Exception raised for errors in the audio processing."""
    def __init__(self, message="Error occurred in audio processing"):
        self.message = message
        super().__init__(self.message)

class DocumentProcessingError(Exception):
    """Exception raised for errors in the document processing."""
    def __init__(self, message="Error occurred in document processing"):
        self.message = message
        super().__init__(self.message)

class OpenAIRequestError(Exception):
    """Exception raised for errors in OpenAI API requests."""
    def __init__(self, message="Error occurred in OpenAI API request"):
        self.message = message
        super().__init__(self.message)

class FileHandlingError(Exception):
    """Exception raised for errors in file handling."""
    def __init__(self, message="Error occurred in file handling"):
        self.message = message
        super().__init__(self.message)

