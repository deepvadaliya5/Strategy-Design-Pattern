from strategies.model_strategy import ModelStrategy


class AIService:

    def __init__(self, model: ModelStrategy):
        self.model = model

    def set_model(self, model: ModelStrategy):
        self.model = model

    def chat(self, prompt: str):
        return self.model.generate(prompt)