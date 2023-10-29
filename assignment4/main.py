from online_store import OnlineStore
from customer import Customer
from discount_observer import DiscountObserver

store = OnlineStore()

customer1 = Customer("Клиент 1")
customer2 = Customer("Клиент 2")

store.add_subscriber(customer1)
store.add_subscriber(customer2)

discount_observer = DiscountObserver()
discount_observer.update(50)
store.announce_discount(10)
store.announce_discount(20)
