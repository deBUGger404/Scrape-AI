from .base import BaseLLM
from anthropic import Anthropic

class AnthropicLLM(BaseLLM):
    def __init__(self, config):
        self.client = Anthropic(api_key=config['api_key'])
        self.model = config['model'].split('/')[-1]

    def chat_completions_create(self, messages, **kwargs):
        return self.client.messages.create(model=self.model, messages=messages, **kwargs)