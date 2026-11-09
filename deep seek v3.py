import os
import requests
from .base_adapter import BaseAdapter


class DeepSeekAdapter(BaseAdapter):

  def __init__(self, model_name: str = "deepseek-chat"):
    self.api_key = os.environ["DEEPSEEK_API_KEY"]
    self.model = model_name
    self.url = "https://api.deepseek.com/v1/chat/completions"

  def generate_text(self, prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": self.model,
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(self.url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]