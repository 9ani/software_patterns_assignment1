class CurrencyConverter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def convert(self, amount):
        return self.strategy.convert(amount)
