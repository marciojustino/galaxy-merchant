import roman_numeral as RomanNumeral
import galactic_numeral as GalacticNumeral
import metal as Metal
import transaction_token as TransactionToken
import galaxy_merchant_exception as GalaxyMerchantException


class GalaxyMerchantTransaction:
    TOKEN_IS = 'is'
    TOKEN_CREDITS = 'Credit'
    TOKEN_HOW = 'how'
    TOKEN_MUCH = 'much'
    TOKEN_MANY = 'many'
    TOKEN_QUESTION = '?'

    transactionOperators = []
    step = 0
    galacticsSequence = 0

    def __init__(self):
        self.__transaction_tokens()
        self.__create_roman_numerals()
        self.__create_galactic_numerals()
        self.__create_metals()
        self.stepFunctions = {
            -1: __step_error,
            1: __step_1,
            2: __step_2,
            3: __step_3,
            4: __step_4,
            5: __step_5,
            6: __step_6,
            7: __step_7,
            8: __step_8,
            9: __step_9,
            10: __step_10,
            11: __step_11,
            12: __step_12,
            13: __step_13,
            14: __step_14,
            15: __step_15,
            16: __step_16,
            17: __step_17,
            999: __step_final
        }

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
        glob = GalacticNumeral(
            'glob', [x for x in self.romanNumerals if x.symbol == 'I'])
        prok = GalacticNumeral(
            'prok', [x for x in self.romanNumerals if x.symbol == 'V'])
        pish = GalacticNumeral(
            'pish', [x for x in self.romanNumerals if x.symbol == 'X'])
        tegj = GalacticNumeral(
            'tegj', [x for x in self.romanNumerals if x.symbol == 'L'])
        self.galacticNumerals = [glob, prok, pish, tegj]

    def __create_metals(self):
        silver = Metal('Silver', 17)
        gold = Metal('Gold', 14450)
        iron = Metal('Iron', 195.5)
        self.metals = [silver, gold, iron]

    def __translate_transaction(self, term):
        func = self.stepFunctions.get(self.step)
        return func(term, self.step)

    def process(self, terms):
        for t in terms:
            self.__translate_transaction(t)

    def __is_galactict(self, term):
        return [x for x in self.galacticNumerals if x.symbol == term]

    def __get_galactict(self, term):
        return [x for x in self.galacticNumerals if x.symbol == term]

    def __is_metal(self, term):
        return [x for x in self.metals if x.symbol == term]

    def __get_metal(self, term):
        return [x for x in self.metals if x.symbol == term]

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

    def __calculate_metal_value():
        # todo: transform galactic values and calculate metal value of transaction
        return

    def __solve_expression(self, expression):
        return 0

    def __step_error(self):
        """ final flow: ERROR """
        raise GalaxyMerchantException()

    def __step_1(self, term):
        if self.__is_galactict(term):
            self.transactionOperators.append(self.__get_galactict(term))
            self.step = 2
        elif term == self.TOKEN_HOW:
            self.transactionOperators.append(term)
            self.step = 10
        else:
            self.step = -1

    def __step_2(self, term):
        if self.__is_galactict(term):
            self.transactionOperators.append(self.__get_galactict(term))
            self.step = 3
        elif term == self.TOKEN_IS:
            self.transactionOperators.append(term)
            self.step = 8

    def __step_3(self, term):
        if self.__isMetal(term):
            self.transactionOperators.append(self.__get_metal(term))
            self.step = 4
        else:
            self.step = -1  # error flow

    def __step_4(self, term):
        if term == self.TOKEN_IS:
            self.transactionOperators.append(term)
            self.step = 5
        else:
            self.step = -1

    def __step_5(self, term):
        if self.__is_number(term):
            self.transactionOperators.append(self.__get_number(term))
            self.step = 6
        else:
            self.step = -1

    def __step_6(self, term):
        if term == self.TOKEN_CREDITS:
            self.transactionOperators.append(term)
            self.step = 7
        else:
            self.step = -1

    def __step_7(self):
        """ finish flow: SUCCESS """
        # todo: set metal value on transactionOperators when calculate
        self.__calculate_metal_value(self.transactionOperators)

    def __step_8(self, term):
        if term == self.TOKEN_IS:
            self.transactionOperators.append(term)
            self.step = 9
        else:
            self.step = -1

    def __step_9(self):
        """ finish flow: SUCCESS """
        # todo: set galactic value on transactionOperators
        self.__set_galactict_value(self.transactionOperators)

    def __step_10(self, term):
        if term == self.TOKEN_MUCH:
            self.transactionOperators.append(term)
            self.step = 11
        elif term == self.TOKEN_MANY:
            self.transactionOperators.append(term)
            self.step = 14
        else:
            self.step = -1

    def __step_11(self, term):
        if term == self.TOKEN_IS:
            self.transactionOperators.append(term)
            self.step = 12
        else:
            self.step = 13  # error flow

    def __step_12(self, term):
        if self.__is_galactict(term):
            if self.galacticsSequence <= 4:
                self.transactionOperators.append(
                    self.__get_galactict_operator(term))
                self.galacticsSequence += 1
            else:
                step = -1  # error flow
        elif term == self.TOKEN_QUESTION:
            self.transactionOperators.append(term)
            self.galacticsSequence = 0
            self.step = 999 # finish flow
        else:
            self.step = -1  # error flow

    def __step_14(self, term):
        if term == TOKEN_CREDITS:
            self.transactionOperators.append(term)
            self.step = 15
        else:
            self.step = -1

    def __step_15(self, term):
        if term == TOKEN_IS:
            self.transactionOperators.append(term)
            self.step = 16
        else:
            self.step = -1

    def __step_16(self, term):
        if self.__is_galactict(term):
            if self.galacticsSequence <= 2:
                self.transactionOperators.append(self.__get_galactict(term))
                self.galacticsSequence += 1
            else:
                self.step = -1
        elif self.__is_metal(term):
            self.transactionOperators.append(self.__get_metal(term))
            self.step = 17
        else:
            self.step = -1  # error flow

    def __step_17(self, term):
        if term == TOKEN_QUESTION:
            self.transactionOperators.append(term)
            self.step = 999 # finish flow
        else:
            self.step = -1  # error flow

    def __step_final(self):
        """ final flow: SUCCESS """
        # todo: calculate many credits in galacticts with metal
        self.__solve_expression(self.transactionOperators)