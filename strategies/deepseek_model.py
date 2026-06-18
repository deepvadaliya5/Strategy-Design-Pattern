from strategies.model_strategy import ModelStrategy


class DeepSeekModel(ModelStrategy):

    def generate(self, prompt: str):
        return f"DeepSeek Response for: {prompt}"