class PackagingDecorator:
    def __init__(self, dress):
        self._dress = dress

    def decorate(self):
        return f"{self._dress} with Package"