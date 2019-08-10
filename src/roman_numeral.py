class RomanNumeral:
    def __init__(self, symbol, value, isRepeatable=False):
        self.symbol = symbol
        self.value = value
        self.isRepeatable = isRepeatable
        self.subtracts = []

    def get_subtract(self, romanSubtract):
        if not isinstance(romanSubtract, RomanNumeral):
            return None

        result = [r for r in self.subtracts if r.symbol == romanSubtract.symbol]
        if result:
            return result[0]
        else:
            return None

    def get_subtracts(self):
        return self.subtracts

    def is_subtract(self, romanNumeral):
        if not isinstance(romanNumeral, RomanNumeral):
            raise TypeError()

        if self.get_subtract(romanNumeral):
            return True
        else:
            return False

    @staticmethod
    def int_to_roman(input):
        if not isinstance(input, type(1)):
            raise TypeError('Expected integer, got %s' % type(input))
        if not 0 < input < 4000:
            raise ValueError('Argument must be between 1 and 3999')

        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count

        return ''.join(result)

    @staticmethod
    def roman_to_int(input):
        input = input.upper()
        nums = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        sum = 0
        for i in range(len(input)):
            try:
                value = nums[input[i]]
                # If the next place holds a larger number, this value is negative
                if i + 1 < len(input) and nums[input[i + 1]] > value:
                    sum -= value
                else:
                    sum += value
            except KeyError:
                raise ValueError('input is not a valid Roman numeral: %s' % input)

        # validate
        if RomanNumeral.int_to_roman(sum) == input:
            return sum
        else:
            raise ValueError('input is not a valid Roman numeral: %s' % input)
