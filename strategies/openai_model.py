from strategies.model_strategy import ModelStrategy


class OpenAIModel(ModelStrategy):

    def generate(self, prompt: str) -> str:
        return f"OpenAI Response for: {prompt}"