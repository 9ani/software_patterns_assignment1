from payment_strategy import PaymentStrategy


class CashOnDeliveryStrategy(PaymentStrategy):
    def pay(self,amount):
        print(f"paid ${amount} using cash on delivery")