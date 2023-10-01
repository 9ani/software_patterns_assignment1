from abc import ABC, abstractmethod
class CurrencyExchangeStrategy(ABC):
    @abstractmethod
    def convert(self, amount):
        pass