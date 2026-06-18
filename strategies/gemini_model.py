from strategies.model_strategy import ModelStrategy


class GeminiModel(ModelStrategy):

    def generate(self, prompt: str) -> str:
        return f"Gemini Response for: {prompt}"