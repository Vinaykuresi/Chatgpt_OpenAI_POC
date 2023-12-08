import docx
from io import BytesIO
from exceptions.custom_exceptions import DocumentProcessingError, FileHandlingError

def read_word_document(file_bytes):
    """
    Reads a Word document from bytes and extracts its text.

    :param file_bytes: The bytes of the Word document.
    :return: Extracted text from the document.
    """
    try:
        doc = docx.Document(BytesIO(file_bytes))
        full_text = [para.text for para in doc.paragraphs]
        return '\n'.join(full_text)
    except Exception as e:
        raise DocumentProcessingError(f"Error reading Word document: {str(e)}")

def save_document_to_file(document_content, file_path):
    """
    Saves the given document content to a file.

    :param document_content: The content to be saved.
    :param file_path: The path where the file will be saved.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(document_content)
    except Exception as e:
        raise FileHandlingError(f"Error saving document to file: {str(e)}")

