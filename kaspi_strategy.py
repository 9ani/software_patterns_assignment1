from payment_strategy import PaymentStrategy

class KaspiStrategy(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount} tenge using Kaspi")