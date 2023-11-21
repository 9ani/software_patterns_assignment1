from  credit_card_strategy import CreditCardStrategy
from kaspi_strategy import KaspiStrategy
from cash_on_delivery_strategy import CashOnDeliveryStrategy


class PaymentAdapter:
    @staticmethod
    def select_payment_method(method):
        if method =="Credit Card":
            return CreditCardStrategy()
        elif method =="Kaspi":
            return KaspiStrategy()
        elif method=="Cash on Delivery":
            return CashOnDeliveryStrategy()
        else:
            raise ValueError("Invalid payment method")
