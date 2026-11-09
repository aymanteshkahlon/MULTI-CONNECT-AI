import os
import google.generativeai as genai
from .base_adapter import BaseAdapter


class GeminiAdapter(BaseAdapter):

  def __init__(self, model_name: str = "gemini-1.5-pro"):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    self.model = genai.GenerativeModel(model_name)

  def generate_text(self, prompt: str) -> str:
    response = self.model.generate_content(prompt)
    return response.text
