
class OnlineStore:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, discount):
        for subscriber in self.subscribers:
            subscriber.update(discount)

    def announce_discount(self, discount):
        print(f"Новая скидка: {discount}%")
        self.notify_subscribers(discount)
