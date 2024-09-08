from .openai_llm import OpenAILLM
from .azure_openai_llm import AzureOpenAILLM
from .anthropic_llm import AnthropicLLM
from .google_llm import GoogleLLM

class LLMFactory:
    @staticmethod
    def create_llm(config):
        provider = config['model'].split('/')[0]
        if provider == 'azure-openai':
            return AzureOpenAILLM(config)
        elif provider == 'anthropic':
            return OpenAILLM(config)
        elif provider == 'anthropic':
            return AnthropicLLM(config)
        elif provider == 'google':
            return GoogleLLM(config)
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")