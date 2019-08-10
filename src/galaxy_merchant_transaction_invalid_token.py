from src.galaxy_merchant_transaction_exception import GalaxyMerchantTransactionException


class GalaxyMerchantTransactionInvalidTokenException(GalaxyMerchantTransactionException):
    def __init__(self, message='Invalid transaction token for transaction'):
        return super().__init__(message=message)