from CurrencyExchangeStrategy import CurrencyExchangeStrategy

class USDtoTNGExchange(CurrencyExchangeStrategy):
    def convert(self, amount):
        return round(amount * 478,79)
