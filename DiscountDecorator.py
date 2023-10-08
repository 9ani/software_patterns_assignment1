from CartDecorator import CartDecorator

class DiscountDecorator(CartDecorator):
    def __init__(self, cart_component, discount_percentage):
        super().__init__(cart_component)
        self._discount_percentage = discount_percentage

    def get_description(self):
        return self._cart_component.get_description() + f" - {self._discount_percentage}% Discount"

    def get_cost(self):
        discount = (self._discount_percentage / 100) * self._cart_component.get_cost()
        return self._cart_component.get_cost() - discount
