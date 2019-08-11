from src.merchant.galaxy_merchant_exception import GalaxyMerchantException


class GalacticNumeralException(GalaxyMerchantException):
    def __init__(self, message='Galactic numeral general error'):
        return super().__init__(message)
