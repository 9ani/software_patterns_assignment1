from dress import Dress

class DressFactory:
    def create_dress(self, category, name, price):
        return Dress(category, name, price)
