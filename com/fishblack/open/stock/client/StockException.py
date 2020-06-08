class StockException(Exception):

    def __init__(self, error):
        super().__init__(self)
        self.errorInfo = error

    def __str__(self):
        return self.errorInfo
