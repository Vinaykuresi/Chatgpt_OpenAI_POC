import openai
import os
import logging
from dependencies import get_openai_client
from exceptions.custom_exceptions import OpenAIRequestError

class OpenAIService:
    def __init__(self):
        self.client = get_openai_client()
        
    def generate_text(self, prompt, model="text-davinci-003", max_tokens=100, temperature=1, **kwargs):
        """
        Generates text based on the given prompt using OpenAI's GPT model.

        :param prompt: The prompt to generate text for.
        :param model: The model to use for text generation.
        :param max_tokens: The maximum number of tokens to generate.
        :param temperature: The temperature to use for the generation.
        :param kwargs: Additional parameters for the OpenAI API.
        :return: Generated text.
        """
        try:
            # Check if the model is one of the newer models
            if model in ["gpt-4", "gpt-4 turbo", "gpt-3.5-turbo"]:
                response = self.client.ChatCompletion.create(
                    model=model,
                    messages=[{"role": "system", "content": prompt}]
                )
            else:
                # For legacy models
                response = self.client.completions.create(
                    model=model,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    **kwargs
                )
        except Exception as e:
            raise OpenAIRequestError(f"Error in generating text: {str(e)}")
        
        return response.choices[0].text.strip()
 
    def transcribe_audio(self, audio_data, model="whisper-1", prompt="", **kwargs):

        try:
            transcript = self.client.audio.transcriptions.create(
                model=model, 
                file=audio_data,
                **kwargs
            )
        except Exception as e:
            raise OpenAIRequestError(f"Error in transcribing audio file: {str(e)}")
        
        return transcript['text']
    
    def corrected_audio(self, temperature, system_prompt, transcribed_text, model, **kwargs):
        try:
            response = self.client.Completion.create(
                model=model,
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
                ],
                **kwargs
            )
        except Exception as e:
            raise OpenAIRequestError(f"Error in transcribing audio file: {str(e)}")
        
        return response.choices[0].message.content


    def summarize_text(self, text, model="text-davinci-003", max_tokens=100):
        """
        Summarizes the given text using OpenAI's GPT model.

        :param text: The text to summarize.
        :param model: The model to use for summarization.
        :param max_tokens: The maximum number of tokens for the summary.
        :return: Summarized text.
        """
        summary_prompt = f"Summarize the following text:\n\n{text}"
        return self.generate_text(summary_prompt, model=model, max_tokens=max_tokens)

    def translate_text(self, text, target_language, model="text-davinci-003"):
        """
        Translates the given text to the target language using OpenAI's GPT model.

        :param text: The text to translate.
        :param target_language: The language to translate the text into.
        :param model: The model to use for translation.
        :return: Translated text.
        """
        translate_prompt = f"Translate the following text to {target_language}:\n\n{text}"
        return self.generate_text(translate_prompt, model=model, max_tokens=250)
