import openai
import os

class OpenAIModel:
    def __init__(self, model_name):
        self.model_name = model_name
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Set the API key globally

    def generate_response(self, query):
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content
