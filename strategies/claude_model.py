from strategies.model_strategy import ModelStrategy


class ClaudeModel(ModelStrategy):

    def generate(self, prompt: str) -> str:
        return f"Claude Response for: {prompt}"