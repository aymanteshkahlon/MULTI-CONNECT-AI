from abc import ABC, abstractmethod


class BaseAdapter(ABC):

    @abstractmethod
    def generate_text( self, prompt: str) -> str:
        """Generate text from a given prompt."""
        pass
