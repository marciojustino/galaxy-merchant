class GalaxyMerchantException(Exception):
    def __init__(self, message='I have no idea what you are talking about'):
        return super().__init__(message)
