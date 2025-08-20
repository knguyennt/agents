from abc import ABC, abstractmethod


class BasePromptStrategy(ABC):
    @abstractmethod
    def create_prompt(self, **kwargs):
        pass