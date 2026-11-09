from src.base_adapter
 import BaseAdapter
from typing import List, Dict


class Orchestrator:

  def __init__(self, adapters: Dict[str, BaseAdapter], verification_agent: BaseAdapter):
    self.adapters = adapters
    self.verification_agent = verification_agent

  def coordinate_debate(self, initial_prompt: str) -> str:
    transcript = f"Initial Goal: {initial_prompt}\n\n"
    for name, adapter in self.adapters.items():
      prompt = f"{transcript}Considering previous insights, provide your analysis and conclusion."
      try:
        response = adapter.generate_text(prompt)
        transcript += f"--- {name.upper()} ---\n{response}\n\n"
      except Exception as e:
        transcript += f"--- {name.upper()} ---\nError: {e}\n\n"
    
    validation_prompt = f"Review the following expert debate and synthesize a final, verified conclusion:\n\n{transcript}"
    final_conclusion = self.verification_agent.generate_text(validation_prompt)
    return final_conclusion