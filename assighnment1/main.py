from USDtoEuroExchange import USDtoEuroExchange
from USDtoTNGExchange import USDtoTNGExchange
from USDtoRUBExchange import USDtoRUBExchange
from CurrencyConverter import CurrencyConverter

if __name__ == "__main__":
    dollars = int(input("Enter the amount of USD dollars: "))

    converter = CurrencyConverter(USDtoEuroExchange())

    euros = converter.convert(dollars)
    print(f"{dollars} USD is equal to {euros} Euros")

    converter.set_strategy(USDtoTNGExchange())
    tenges = converter.convert(dollars)
    print(f"{dollars} USD is equal to {tenges} Tenge")

    converter.set_strategy(USDtoRUBExchange())
    rubles = converter.convert(dollars)
    print(f"{dollars} USD is equal to {rubles} Rubles")
