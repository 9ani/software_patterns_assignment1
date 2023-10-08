from Product import Product
from ShoppingCart import ShoppingCart
from GiftWrapDecorator import GiftWrapDecorator
from DeliveryDecorator import DeliveryDecorator
from DiscountDecorator import DiscountDecorator

if __name__ == "__main__":
    laptop = Product("Laptop", 1000.0)
    phone = Product("Smartphone", 500.0)

    cart = ShoppingCart()
    cart.add_item(laptop)
    cart.add_item(phone)

    cart = GiftWrapDecorator(cart)
    cart = DeliveryDecorator(cart)
    cart = DiscountDecorator(cart, 10)


    print(cart.get_description())
    print(f"Total cost: ${cart.get_cost()}")
