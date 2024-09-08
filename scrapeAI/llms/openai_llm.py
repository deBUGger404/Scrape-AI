from .base import BaseLLM
from openai import OpenAI

class OpenAILLM(BaseLLM):
    def __init__(self, config):
        self.client = OpenAI(api_key=config['api_key'])
        self.model = config['model'].split('/')[-1]

    def chat_completions_create(self, messages, **kwargs):
        return self.client.chat.completions.create(model=self.model, messages=messages, **kwargs)