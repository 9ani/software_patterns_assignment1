from CurrencyExchangeStrategy import CurrencyExchangeStrategy

class USDtoEuroExchange(CurrencyExchangeStrategy):
    def convert(self, amount):
        return round(amount * 0.94)
