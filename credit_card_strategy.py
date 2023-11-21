from payment_strategy import PaymentStrategy


class CreditCardStrategy(PaymentStrategy):
    def pay(self,amount):
        print(f"paid ${amount} using credit card")