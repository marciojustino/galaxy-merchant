from src.roman_numeral_exception import RomanNumeralException

class RomanNumeralInvalidException(RomanNumeralException):
    def __init__(self, message='Roman numeral invalid exception'):
        return super().__init__(message=message)