from pydantic import BaseModel, Field

class DocumentProcessingParameters(BaseModel):
    task: str = Field(default="summarize", description="Processing task to be applied to the document, e.g., 'summarize', 'translate'.")
    # You can add more parameters as needed, such as language, length of summary, etc.

class DocumentRequest(BaseModel):
    content: str
    processing_parameters: DocumentProcessingParameters

class DocumentResponse(BaseModel):
    processed_content: str  # The processed content of the document
