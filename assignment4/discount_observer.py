
from online_store import OnlineStore

class DiscountObserver:
    def __init__(self):
        self.store = OnlineStore()
        self.store.add_subscriber(self)

    def update(self, discount):
        print(f"Уведомление о скидке: {discount}%")

    def announce_discount(self, discount):
        self.store.announce_discount(discount)
