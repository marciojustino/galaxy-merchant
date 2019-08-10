from src.galactic_numeral_exception import GalacticNumeralException


class GalacticNumeralInvalidException(GalacticNumeralException):
    def __init__(self, message=''):
        return super().__init__(message=message)
