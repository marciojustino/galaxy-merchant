from src.roman_numeral import RomanNumeral
from src.galactic_numeral import GalacticNumeral
from src.metal import Metal
from src.transaction_token import TransactionToken
from src.galaxy_merchant_exception import GalaxyMerchantException


class GalaxyMerchantTransaction:
    TOKEN_IS = 'is'
    TOKEN_CREDITS = 'Credits'
    TOKEN_HOW = 'how'
    TOKEN_MUCH = 'much'
    TOKEN_MANY = 'many'
    TOKEN_QUESTION = '?'

    compiledTransaction = []
    compiledTransactions = []
    step = 1
    galacticsSequence = 0

    def __init__(self):
        self.__transaction_tokens()
        self.__create_roman_numerals()
        self.__create_galactic_numerals()
        self.__create_metals()

    def __transaction_tokens(self):
        self.transactionTokens = [
            TransactionToken('is'),
            TransactionToken('Credits')
        ]

    def __create_roman_numerals(self):
        I = RomanNumeral('I', 1, True)
        V = RomanNumeral('V', 5, False)
        X = RomanNumeral('X', 10, True)
        L = RomanNumeral('L', 50, False)
        C = RomanNumeral('C', 100, True)
        D = RomanNumeral('D', 500, False)
        M = RomanNumeral('M', 1000, True)
        I.subtracts = [V, X]
        X.subtracts = [L, C]
        C.subtracts = [D, M]
        self.romanNumerals = [I, V, X, L, C, D, M]

    def __create_galactic_numerals(self):
        self.galacticNumerals = [
            GalacticNumeral('glob', None),
            GalacticNumeral('prok', None),
            GalacticNumeral('pish', None),
            GalacticNumeral('tegj', None)
        ]

    def __create_metals(self):
        self.metals = [
            Metal('Silver', 17),
            Metal('Gold', 14450),
            Metal('Iron', 195.5)
        ]

    def __compile_transaction(self, term):
        func = self.stepFunctions.get(self.step)
        func(self, term)

    def __init_compiler(self):
        self.step = 1
        self.compiledTransaction = []

    def process(self, terms):
        self.__init_compiler()
        for t in terms:
            self.__compile_transaction(t)

    def __is_galactict(self, term):
        return [x for x in self.galacticNumerals if x.symbol == term]

    def __get_galactict(self, term):
        return [x for x in self.galacticNumerals if x.symbol == term][0]

    def __is_roman_numeral(self, term):
        return [x for x in self.romanNumerals if x.symbol == term]

    def __get_roman_numeral(self, term):
        return [x for x in self.romanNumerals if x.symbol == term][0]

    def __is_metal(self, term):
        return [x for x in self.metals if x.symbol == term]

    def __get_metal(self, term):
        return [x for x in self.metals if x.symbol == term][0]

    def __set_metal_value(self, metal: Metal, value):
        [m for m in self.metals if m.symbol == metal.symbol][0].value = value

    def __is_number(self, term):
        try:
            return int(term)
        except ValueError:
            try:
                return float(term)
            except ValueError:
                return False

    def __get_number(self, term):
        return int(term)

    def __calculate_metal_value(self):
        galacticNumerals = [
            g for g in self.compiledTransaction
            if isinstance(g, GalacticNumeral)
        ]
        galacticNumeralsToRomanNumeral = ''
        for g in galacticNumerals:
            galacticNumeralsToRomanNumeral += g.romanNumeral.symbol

        # translate roman value
        decodedGalactictsValue = RomanNumeral.roman_to_int(galacticNumeralsToRomanNumeral)
        totalCredits = [v for v in self.compiledTransaction if isinstance(v, int)][0]
        self.__set_metal_value([m for m in self.compiledTransaction if isinstance(m, Metal)], (decodedGalactictsValue / totalCredits))

    def __set_galactict_value(self):
        [
            x for x in self.galacticNumerals
            if x.symbol == self.compiledTransaction[0].symbol
        ][0].romanNumeral = self.compiledTransaction[2]

    def __solve_expression(self, expression):
        return 0

    def __step_error(self):
        """ final flow: ERROR """
        raise GalaxyMerchantException()

    def __step_1(self, term):
        if self.__is_galactict(term):
            self.compiledTransaction.append(self.__get_galactict(term))
            self.step = 2
        elif term == self.TOKEN_HOW:
            self.compiledTransaction.append(term)
            self.step = 10
        else:
            self.__step_error()  # error flow

    def __step_2(self, term):
        if self.__is_galactict(term):
            self.compiledTransaction.append(self.__get_galactict(term))
            self.step = 3
        elif term == self.TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 8

    def __step_3(self, term):
        if self.__is_metal(term):
            self.compiledTransaction.append(self.__get_metal(term))
            self.step = 4
        else:
            self.__step_error()  # error flow

    def __step_4(self, term):
        if term == self.TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 5
        else:
            self.__step_error()  # error flow

    def __step_5(self, term):
        if self.__is_number(term):
            self.compiledTransaction.append(self.__get_number(term))
            self.step = 6
        else:
            self.__step_error()  # error flow

    def __step_6(self, term):
        if term == self.TOKEN_CREDITS:
            self.compiledTransaction.append(term)
            self.__step_final_7()  # finish flow
        else:
            self.__step_error()  # error flow

    def __step_final_7(self):
        """ finish flow: SUCCESS """
        # todo: set metal value on compiledTransaction when calculate
        self.__calculate_metal_value()
        self.compiledTransactions.append(self.compiledTransaction)

    def __step_8(self, term):
        if self.__is_roman_numeral(term):
            self.compiledTransaction.append(self.__get_roman_numeral(term))
            self.__step_final_9()  # finish flow
        else:
            self.__step_error()  # error flow

    def __step_final_9(self):
        """ finish flow: SUCCESS """
        self.__set_galactict_value()
        self.compiledTransactions.append(self.compiledTransaction)

    def __step_10(self, term):
        if term == self.TOKEN_MUCH:
            self.compiledTransaction.append(term)
            self.step = 11
        elif term == self.TOKEN_MANY:
            self.compiledTransaction.append(term)
            self.step = 14
        else:
            self.__step_error()  # error flow

    def __step_11(self, term):
        if term == self.TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 12
        else:
            self.__step_error()  # error flow

    def __step_12(self, term):
        if self.__is_galactict(term):
            if self.galacticsSequence <= 4:
                self.compiledTransaction.append(
                    self.__get_galactict_operator(term))
                self.galacticsSequence += 1
            else:
                self.__step_error()  # error flow
        elif term == self.TOKEN_QUESTION:
            self.compiledTransaction.append(term)
            self.galacticsSequence = 0
            self.__step_final_13()  # finish flow
        else:
            self.__step_error()  # error flow

    def __step_14(self, term):
        if term == TOKEN_CREDITS:
            self.compiledTransaction.append(term)
            self.step = 15
        else:
            self.__step_error()  # error flow

    def __step_15(self, term):
        if term == TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 16
        else:
            self.__step_error()  # error flow

    def __step_16(self, term):
        if self.__is_galactict(term):
            if self.galacticsSequence <= 2:
                self.compiledTransaction.append(self.__get_galactict(term))
                self.galacticsSequence += 1
            else:
                self.__step_error
        elif self.__is_metal(term):
            self.compiledTransaction.append(self.__get_metal(term))
            self.step = 17
        else:
            self.__step_error()  # error flow

    def __step_17(self, term):
        if term == TOKEN_QUESTION:
            self.compiledTransaction.append(term)
            self.step = 999  # finish flow
        else:
            self.__step_error()  # error flow

    def __step_final_13(self):
        """ final flow: SUCCESS """
        # todo: calculate many credits in galacticts with metal
        self.__solve_expression(self.compiledTransaction)

    stepFunctions = {
        -1: __step_error,
        1: __step_1,
        2: __step_2,
        3: __step_3,
        4: __step_4,
        5: __step_5,
        6: __step_6,
        7: __step_final_7,
        8: __step_8,
        9: __step_final_9,
        10: __step_10,
        11: __step_11,
        12: __step_12,
        999: __step_final_13,
        14: __step_14,
        15: __step_15,
        16: __step_16,
        17: __step_17
    }
