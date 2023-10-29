
class Customer:
    def __init__(self, name):
        self.name = name

    def update(self, discount):
        print(f"{self.name}, новая скидка: {discount}%")
