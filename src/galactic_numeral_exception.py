from src.galaxy_merchant_exception import GalaxyMerchantException

class GalacticNumeralException(GalaxyMerchantException):
    def __init__(self, message='Galactic numeral general exception'):
        return super().__init__(message=message)