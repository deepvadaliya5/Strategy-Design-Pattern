from strategies.gemini_model import GeminiModel
from strategies.openai_model import OpenAIModel
from strategies.claude_model import ClaudeModel

from services.ai_service import AIService


service = AIService(GeminiModel())

print(service.chat("Hello"))

service.set_model(OpenAIModel())

print(service.chat("Hello"))

service.set_model(ClaudeModel())

print(service.chat("Hello"))