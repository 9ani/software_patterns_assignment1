class Dress:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price

    def decorate(self):
        return f"{self.name} Dress"

    def __str__(self):
        return f"{self.name} - {self.price} tenge"