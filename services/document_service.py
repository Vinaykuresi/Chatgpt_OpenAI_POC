

def process_document_logic(openai_client):
    # You can further process the text with OpenAI's API
    response = openai_client.Completion.create(
        engine="text-davinci-003",
        prompt="Summarize this document:\n\n" + document_content,
        max_tokens=100
    )
    document_content = response.choices[0].text.strip()
