import os
from openai import OpenAI
from .base_adapter import BaseAdapter


class ChatGPTAdapter(BaseAdapter):

  def __init__(self, model_name: str = "gpt-4o"):
    self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    self.model = model_name

  def generate_text(self, prompt: str) -> str:
    response = self.client.chat.completions.create(
        model=self.model, messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content