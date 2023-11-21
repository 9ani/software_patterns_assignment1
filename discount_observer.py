class DiscountObserver:
    def __init__(self, email):
        self.email = email

    def update(self, discount):
        print(f"Notification: {discount}% discount is available for {self.email}.")
