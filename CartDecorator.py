from CartComponent import CartComponent

class CartDecorator(CartComponent):
    def __init__(self, cart_component):
        self._cart_component = cart_component

    def get_description(self):
        return self._cart_component.get_description()

    def get_cost(self):
        return self._cart_component.get_cost()
