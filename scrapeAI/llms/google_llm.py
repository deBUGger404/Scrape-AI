from .base import BaseLLM
import google.generativeai as genai

class GoogleLLM(BaseLLM):
    def __init__(self, config):
        genai.configure(api_key=config['api_key'])
        self.model = genai.GenerativeModel(config['model'].split('/')[-1])

    def chat_completions_create(self, messages, **kwargs):
        return self.model.generate_content([m['content'] for m in messages], **kwargs)