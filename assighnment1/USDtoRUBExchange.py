from CurrencyExchangeStrategy import CurrencyExchangeStrategy

class USDtoRUBExchange(CurrencyExchangeStrategy):
    def convert(self, amount):
        return (amount * 98)
