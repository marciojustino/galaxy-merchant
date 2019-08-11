from src.roman.roman_numeral import RomanNumeral
from src.galactic.galactic_numeral import GalacticNumeral
from src.galactic.galactic_numeral_exception import GalacticNumeralException
from src.metal.metal import Metal
from src.merchant.galaxy_merchant_transaction_token import GalaxyMerchantTransactionToken
from src.merchant.galaxy_merchant_exception import GalaxyMerchantException
from src.roman.roman_numeral_invalid_exception import RomanNumeralInvalidException
from src.merchant.galaxy_merchant_transaction_exception import GalaxyMerchantTransactionException
from src.merchant.galaxy_merchant_transaction_invalid_token import GalaxyMerchantTransactionInvalidTokenException


class GalaxyMerchantTransaction:
    TOKEN_IS = 'is'
    TOKEN_CREDITS = 'Credits'
    TOKEN_HOW = 'how'
    TOKEN_MUCH = 'much'
    TOKEN_MANY = 'many'
    TOKEN_QUESTION = '?'

    compiledTransaction = []
    compiledTransactions = []
    resolution = None
    step = 1
    galacticsSequence = 0

    def __init__(self):
        self.__transaction_tokens()
        self.__create_roman_numerals()
        self.__create_galactic_numerals()
        self.__create_metals()

    def __transaction_tokens(self):
        self.transactionTokens = [
            GalaxyMerchantTransactionToken('is'),
            GalaxyMerchantTransactionToken('Credits')
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
            Metal('Silver', None),
            Metal('Gold', 14450),
            Metal('Iron', 195.5)
        ]

    def __compile_transaction(self, term):
        func = self.stepFunctions.get(self.step)
        func(self, term)

    def __init_compiler(self):
        self.step = 1
        self.galacticsSequence = 0
        self.compiledTransaction = []
        self.resolution = None

    def process(self, terms):
        self.__init_compiler()
        for t in terms:
            self.__compile_transaction(t)
        return self.resolution

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

    def __set_metal_value(self, metal: Metal, newValue):
        [m for m in self.metals if m.symbol == metal.symbol][0].value = newValue

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

    def __extract_metal_from_transaction(self):
        return [m for m in self.compiledTransaction if isinstance(m, Metal)][0]

    def __calculate_metal_value(self):
        galacticNumerals = [g for g in self.compiledTransaction if isinstance(g, GalacticNumeral)]
        galacticNumeralsToRomanNumeral = ''
        for g in galacticNumerals:
            galacticNumeralsToRomanNumeral += g.romanNumeral.symbol
        # translate roman value
        decodedGalactictsValue = RomanNumeral.roman_to_int(galacticNumeralsToRomanNumeral)
        totalCredits = [v for v in self.compiledTransaction if isinstance(v, int)][0]
        self.__set_metal_value(self.__extract_metal_from_transaction(), (totalCredits / decodedGalactictsValue))

    def __set_galactict_value(self):
        [x for x in self.galacticNumerals if x.symbol == self.compiledTransaction[0].symbol][0].romanNumeral = self.compiledTransaction[2]

    def __get_count_sequence_roman_numeral_in_transaction(self, galactic: GalacticNumeral):
        indexes = []
        for index, g in enumerate(self.compiledTransaction):
            if isinstance(g, GalacticNumeral) and g.romanNumeral.symbol == galactic.romanNumeral.symbol:
                indexes.append(index)
        founded = 0
        countIndexes = len(indexes)
        subIndexes = countIndexes
        for i in reversed(range(countIndexes)):
            if indexes[i] < subIndexes - 1:
                break
            founded += 1
            subIndexes -= indexes[i]
        return founded

    def __get_last_galactic_in_transaction(self, galactic: GalacticNumeral):
        results = [g for g in self.compiledTransaction if isinstance(g, GalacticNumeral) and g.romanNumeral.symbol == galactic.romanNumeral.symbol]
        if results:
            return results[-1]
        return None

    def __allow_subtract(self, galactic: GalacticNumeral):
        lastGalacticInTransaction = self.__get_last_galactic_in_transaction(galactic)
        if not lastGalacticInTransaction:
            return True
        return galactic.romanNumeral.is_subtract(lastGalacticInTransaction.romanNumeral)

    def __reached_max_repeatable_sequence_roman_numeral_in_transaction(self, galactic: GalacticNumeral):
        return self.__get_count_sequence_roman_numeral_in_transaction(galactic) == 3

    def __check_possible_subtract(self, galactic: GalacticNumeral):
        lastGalacticInTransaction = self.__get_last_galactic_in_transaction(galactic)
        if not lastGalacticInTransaction:
            return
        if galactic.romanNumeral.symbol == lastGalacticInTransaction.romanNumeral.symbol:
            return
        if galactic.romanNumeral.is_subtract(lastGalacticInTransaction.romanNumeral):
            return
        raise RomanNumeralInvalidException()

    def __validate_roman_numeral_repetitions(self, galactic: GalacticNumeral):
        self.__check_possible_subtract(galactic)
        countSequenceRomanNumeralInTransaction = self.__get_count_sequence_roman_numeral_in_transaction(galactic)
        if countSequenceRomanNumeralInTransaction >= 1:
            # allow insert until 3 roman numerals in sequence
            if not galactic.romanNumeral.isRepeatable:
                raise RomanNumeralInvalidException('Roman numeral {} is not repeatable'.format(galactic.romanNumeral.symbol))
            if self.__reached_max_repeatable_sequence_roman_numeral_in_transaction(galactic):
                raise RomanNumeralInvalidException('Max repeatable sequencial roman numeral {} reached'.format(galactic.romanNumeral.symbol))

    def __get_all_galactics_in_compiled_transaction(self):
        return [token for token in self.compiledTransaction if isinstance(token, GalacticNumeral)]

    def __get_all_metals_in_compiled_transaction(self):
        return [token for token in self.compiledTransaction if isinstance(token, Metal)]

    def __solve_how_much_transaction(self):
        allGalacticNumerals = self.__get_all_galactics_in_compiled_transaction()
        romanString = GalacticNumeral.to_roman_string(allGalacticNumerals)
        total = RomanNumeral.roman_to_int(romanString)
        self.resolution = '{} is {}'.format(GalacticNumeral.only_symbols(allGalacticNumerals), total)

    def __solve_how_many_transaction(self):
        allGalacticNumerals = self.__get_all_galactics_in_compiled_transaction()
        romanString = GalacticNumeral.to_roman_string(allGalacticNumerals)
        metals = self.__get_all_metals_in_compiled_transaction()
        total = RomanNumeral.roman_to_int(romanString)
        for m in metals:
            total *= m.value
        self.resolution = '{} is {} Credits'.format(GalacticNumeral.only_symbols(allGalacticNumerals), total)

    def __step_error(self, error: GalaxyMerchantTransactionException):
        """ final flow: ERROR """
        raise GalaxyMerchantTransactionException()

    def __step_1(self, term):
        if self.__is_galactict(term):
            self.compiledTransaction.append(self.__get_galactict(term))
            self.step = 2
        elif term == self.TOKEN_HOW:
            self.compiledTransaction.append(term)
            self.step = 10
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected "galactic" or "how" not found'))  # error flow

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
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected "metal" not found'))  # error flow

    def __step_4(self, term):
        if term == self.TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 5
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "is" not found'))  # error flow

    def __step_5(self, term):
        if self.__is_number(term):
            self.compiledTransaction.append(self.__get_number(term))
            self.step = 6
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected value not found'))  # error flow

    def __step_6(self, term):
        if term == self.TOKEN_CREDITS:
            self.compiledTransaction.append(term)
            self.__step_final_7()  # finish flow
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "Credits" not found'))  # error flow

    def __step_final_7(self):
        """ finish flow: SUCCESS """
        self.__calculate_metal_value()
        self.compiledTransactions.append(self.compiledTransaction)

    def __step_8(self, term):
        if self.__is_roman_numeral(term):
            self.compiledTransaction.append(self.__get_roman_numeral(term))
            self.__step_final_9()  # finish flow
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected "roman numeral" not found'))  # error flow

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
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "much" or "many" not found'))  # error flow

    def __step_11(self, term):
        if term == self.TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 12
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "is" not found'))  # error flow

    def __step_12(self, term):
        if self.__is_galactict(term):
            if self.galacticsSequence <= 6:
                # allow insert until 7 galactic numerals in transaction
                galactic = self.__get_galactict(term)
                if self.galacticsSequence >= 1:
                    self.__validate_roman_numeral_repetitions(galactic)
                self.galacticsSequence += 1
                self.compiledTransaction.append(galactic)
            else:
                self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Max of "galactic" in a row reached (7)'))  # error flow
        elif term == self.TOKEN_QUESTION:
            if self.galacticsSequence < 2:
                raise GalacticNumeralException('Expected at least 2 galactics in a row but only 1 found')
            self.compiledTransaction.append(term)
            self.__step_final_13()  # finish flow
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected "galactic" or token "?" not found'))  # error flow

    def __step_14(self, term):
        if term == self.TOKEN_CREDITS:
            self.compiledTransaction.append(term)
            self.step = 15
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "Credits" not found'))  # error flow

    def __step_15(self, term):
        if term == self.TOKEN_IS:
            self.compiledTransaction.append(term)
            self.step = 16
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "is" not found'))  # error flow

    def __step_16(self, term):
        if self.__is_galactict(term):
            if self.galacticsSequence <= 6:
                galactic = self.__get_galactict(term)
                if self.galacticsSequence >= 1:
                    self.__validate_roman_numeral_repetitions(galactic)
                self.galacticsSequence += 1
                self.compiledTransaction.append(galactic)
            else:
                self.__step_error()  # error flow
        elif self.__is_metal(term):
            self.compiledTransaction.append(self.__get_metal(term))
            self.step = 17
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected an "galactic" or "metal" not found'))  # error flow

    def __step_17(self, term):
        if term == self.TOKEN_QUESTION:
            self.compiledTransaction.append(term)
            self.__step_final_18()  # finish flow
        else:
            self.__step_error(GalaxyMerchantTransactionInvalidTokenException('Expected token "?" not found'))  # error flow

    def __step_final_18(self):
        """ final flow: SUCCESS """
        self.__solve_how_many_transaction()
        self.compiledTransactions.append(self.compiledTransaction)

    def __step_final_13(self):
        """ final flow: SUCCESS """
        self.__solve_how_much_transaction()
        self.compiledTransactions.append(self.compiledTransaction)

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
        13: __step_final_13,
        14: __step_14,
        15: __step_15,
        16: __step_16,
        17: __step_17,
        18: __step_final_18
    }
