from CartComponent import CartComponent

class ShoppingCart(CartComponent):
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def get_description(self):
        description = "Shopping Cart:\n"
        for item in self.items:
            description += item.get_description() + "\n"
        return description

    def get_cost(self):
        return sum(item.get_cost() for item in self.items)
