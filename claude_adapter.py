import os
from anthropic import Anthropic
from .base_adapter import BaseAdapter


class ClaudeAdapter(BaseAdapter):

  def __init__(self, model_name: str = "claude-3-5-sonnet-20241022"):
    self.client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    self.model = model_name

  def generate_text(self, prompt: str) -> str:
    response = self.client.messages.create(
        model=self.model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text