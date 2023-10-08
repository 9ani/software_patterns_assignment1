from CartComponent import CartComponent

class Product(CartComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return f"{self.name}: ${self.price}"

    def get_cost(self):
        return self.price
