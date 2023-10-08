from CartDecorator import CartDecorator

class GiftWrapDecorator(CartDecorator):
    def get_description(self):
        return self._cart_component.get_description() + " + Gift Wrapping"

    def get_cost(self):
        return self._cart_component.get_cost() + 5.0
