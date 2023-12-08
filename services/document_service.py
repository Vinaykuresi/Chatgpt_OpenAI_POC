from .openai_service import OpenAIService
from exceptions.custom_exceptions import DocumentProcessingError

class DocumentService:
    def __init__(self):
        self.openai_service = OpenAIService()

    def process_document_logic(self, document_content, task="summarize", model="text-davinci-003", max_tokens=100):
        """
        Processes the document content using OpenAI's API based on the specified task.

        :param openai_client: The OpenAI client.
        :param document_content: The content of the document to process.
        :param task: The processing task (e.g., "summarize").
        :param model: The OpenAI model to use.
        :param max_tokens: The maximum number of tokens for the response.
        :return: The processed text.
        """
        prompt = f"{task} this document:\n\n{document_content}"
        try:
            response = self.openai_service.generate_text(prompt, model, max_tokens)
            return response
        except Exception as e:
             raise DocumentProcessingError(f"Error processing document: {str(e)}")