from transformers import pipeline
import warnings
from typing import List, Dict, Any


class ExcuseGenerator:
    def __init__(self, model_name: str = "distilgpt2"):
        """
        Initialize with either specified model or fallback to mock generator.
        """
        self.model_name = model_name
        self.using_mock = False
        self._pipeline = pipeline  # Store original pipeline reference

        try:
            self.generator = self._create_real_generator()
        except Exception as e:
            warnings.warn(f"Model load failed: {e}. Using mock generator.")
            self.generator = self._mock_generator
            self.using_mock = True

    def _create_real_generator(self):
        """Separate method for easier mocking in tests"""
        return self._pipeline("text-generation", model=self.model_name)

    @staticmethod
    def _mock_generator(prompt: str, **kwargs) -> List[Dict[str, str]]:
        """Mock generator with testable output"""
        return [{"generated_text": f"[MOCK] Excuse for: {prompt}"}]

    def generate(self, scenario: str, details: str) -> str:
        """Generate excuse for given context"""
        prompt = f"{scenario} excuse: {details}"
        result = self.generator(prompt, max_length=100)
        return result[0]['generated_text']