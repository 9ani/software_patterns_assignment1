from dress import Dress
from dress_factory import DressFactory
from discount_observer import DiscountObserver
from discount_subject import DiscountSubject
from payment_adapter import PaymentAdapter
from decoration_factory import DecorationFactory


class UserInterface:
    def __init__(self, dress_factory: DressFactory):
        self.discount_subject = DiscountSubject()
        self.dress_factory = dress_factory
        self.cart = []
        self.payment_adapter=PaymentAdapter()
        self.decoration_factory = DecorationFactory()

    def set_discount_subject(self, discount_subject: DiscountSubject):
        self.discount_subject = discount_subject

    def display_menu(self):
        while True:
            print("Welcome to Zaida Dress - Online Dress Shop")
            print("1. Browse Categories")
            print("2. Subscribe for Discounts")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")

            choice = input("Select an option: ")
            if choice == "1":
                self.browse_categories()

            elif choice=="2":
                self.subscribe_for_discounts()
            elif choice=="3":
                self.view_cart()
            elif choice=="4":
                self.checkout()
            elif choice == "5":
                print("Thank you for visiting Zaida Dress.Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option!")

    def browse_categories(self):
        print("Browsing Categories...")
        categories = ["Evening Dresses" , "Wedding Dresses", "Party Dresses"]
        print("Available Dress Categories:")
        for index,category in enumerate(categories,start=1):
            print(f"{index}. {category}")
        category_choice = input("Select a category (enter the number): ")

        try:
            category_choice = int(category_choice)
            if 1 <= category_choice <= len(categories):
                selected_category=categories[category_choice - 1]
                print(f"You have selected the '{selected_category}' category.")
                self.display_dresses_in_category(selected_category)
            else:
                print("Invalid category number. Please, select a valid one!!!")
        except ValueError:
            print("Invalid input.")

    def display_dresses_in_category(self, category):
        dresses = [
            self.dress_factory.create_dress("Evening Dresses", "Elegant Evening Gown", 10000),
            self.dress_factory.create_dress("Wedding Dresses", "White Lace Wedding Dress", 15000),
            self.dress_factory.create_dress("Party Dresses", "Sparkling Party Dress", 20000),
            self.dress_factory.create_dress("Evening Dresses", "Satin Evening Dress", 12000),
            self.dress_factory.create_dress("Wedding Dresses", "Vintage Wedding Dress", 18000),
            self.dress_factory.create_dress("Party Dresses", "Floral Print Party Dress", 16000),
            self.dress_factory.create_dress("Evening Dresses", "Velvet Evening Gown", 13000),
            self.dress_factory.create_dress("Wedding Dresses", "Mermaid Wedding Dress", 20000),
            self.dress_factory.create_dress("Party Dresses", "Sequin Party Dress", 22000),
        ]

        print(f"Dresses in the '{category}' category: ")
        category_dresses = [dress for dress in dresses if dress.category == category]

        for index, dress in enumerate(category_dresses, start=1):
            print(f"{index}. {dress}")

        dress_choice = input("Select a dress (enter the number): ")

        try:
            dress_choice = int(dress_choice)
            if 1 <= dress_choice <= len(category_dresses):
                selected_dress = category_dresses[dress_choice - 1]
                print(f"You have selected the '{selected_dress.name}' dress.")
                self.add_to_cart(selected_dress)
            else:
                print("Invalid dress number. Please, enter a valid one!!!")
        except ValueError:
            print("Invalid input")

    def add_to_cart(self, dress):
        decorated_dress = self.decorate_dress(dress)
        self.cart.append(
            (dress, decorated_dress))
        print(f"'{dress.name} - ${dress.price}' added to your cart.")

    def view_cart(self):
        print("Your cart: ")
        if not self.cart:
            print("Your cart is empty. ")
        else:
            for index, item in enumerate(self.cart,start=1):
                print(f"{index}. {item}")

    def subscribe_for_discounts(self):
        if self.discount_subject:
            print("Subscribe for Discounts...")
            email = input("Enter your email address to subscribe: ")
            self.discount_subject.add_observer(DiscountObserver(email))
            print("You have been subscribed for discounts. ")
        else:
            print("discount subscription is currently unavailable")

    def decorate_dress(self, dress):
        print("Available Decoration: ")
        print("1. Jewelry")
        print("2. Packaging")
        choices = map(int,input("Select decorations to add (comma-separated, e.g., '1,2'): ").split(','))

        decorated_dress = dress

        for choice in choices:
            try:
                choice = int(choice)
                if choice == 1:
                    decorated_dress = self.decoration_factory.create_jewelry_decorator(decorated_dress).decorate()
                elif choice == 2:
                    decorated_dress = self.decoration_factory.create_packaging_decorator(decorated_dress).decorate()
                else:
                    print(f"Ignoring invalid decoration choice: {choice}")
            except ValueError:
                print(f"Ignoring non-integer decoration choice: {choice}")
        return decorated_dress

    def checkout(self):
        print("Checkout: ")
        self.view_cart()

        total_price = sum(
            int(item[0].price) for item in self.cart)

        print(f"Total Price: {total_price} tenge")

        payment_method = input("Select payment method (Credit Card, Kaspi, Cash on delivery): ")
        payment_strategy = self.payment_adapter.select_payment_method(payment_method)

        payment_strategy.pay(total_price)
        self.discount_subject.notify_observers(10)

        print("Thank you for shopping with Zaida Dress!!!")
        self.cart = []