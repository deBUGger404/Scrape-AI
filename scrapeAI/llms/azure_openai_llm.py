from .base import BaseLLM
from openai import AzureOpenAI

class AzureOpenAILLM(BaseLLM):
    def __init__(self, config):
        self.client = AzureOpenAI(
            api_key=config['api_key'],
            api_version=config['api_version'],
            azure_endpoint=config['endpoint']
        )
        self.model = config['model'].split('/')[-1]

    def chat_completions_create(self, messages, **kwargs):
        return self.client.chat.completions.create(model=self.model, messages=messages, **kwargs)