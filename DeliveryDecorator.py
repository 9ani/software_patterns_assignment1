from CartDecorator import CartDecorator

class DeliveryDecorator(CartDecorator):
    def get_description(self):
        return self._cart_component.get_description() + " + Delivery"

    def get_cost(self):
        return self._cart_component.get_cost() + 10.0
