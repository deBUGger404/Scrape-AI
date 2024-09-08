from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def chat_completions_create(self, messages, **kwargs):
        pass