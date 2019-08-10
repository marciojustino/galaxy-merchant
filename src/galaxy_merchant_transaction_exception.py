from src.galaxy_merchant_exception import GalaxyMerchantException


class GalaxyMerchantTransactionException(GalaxyMerchantException):
    def __init__(self, message='I have no idea what you are talking about'):
        super().__init__(message)
