import os
import google.generativeai as genai
from .base_adapter import BaseAdapter


class LlamaAdapter(BaseAdapter):

  def __init__(self, model_name: str = "llama-3.3-70b-versatile"):
    self.client = genai.Client(api_key=os.environ["GROQ_API_KEY"])
    self.model = model_name

  def generate_text(self, prompt: str) -> str:
    response = self.client.models.generate_content(
        model=self.model,
        contents=prompt,
    )
    return response.text