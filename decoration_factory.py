from jewelry_decorator import JewelryDecorator
from packaging_decorator import PackagingDecorator


class DecorationFactory:
    def create_jewelry_decorator(self, dress):
        return JewelryDecorator(dress)
    def create_packaging_decorator(self, dress):
        return PackagingDecorator(dress)