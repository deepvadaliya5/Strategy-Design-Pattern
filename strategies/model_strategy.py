from abc import ABC, abstractmethod


class ModelStrategy(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass