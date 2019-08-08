import roman_numeral as RomanNumeral
import galactic_numeral as GalacticNumeral
import metal as Metal

class GalacticMerchant:
    def __init__(self):
        self.createRomanNumerals()
        self.createGalacticNumerals()

    def createRomanNumerals(self):
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
    
    def createGalacticNumerals(self):
        glob = GalacticNumeral('glob', [x for x in self.romanNumerals if x.symbol == 'I'])
        prok = GalacticNumeral('prok', [x for x in self.romanNumerals if x.symbol == 'V'])
        pish = GalacticNumeral('pish', [x for x in self.romanNumerals if x.symbol == 'X'])
        tegj = GalacticNumeral('tegj', [x for x in self.romanNumerals if x.symbol == 'L'])

        self.galacticNumerals = [glob, prok, pish, tegj]

    def createMetals(self):
        silver = Metal('Silver', 17)
        gold = Metal('Gold', 14450)
        iron = Metal('Iron', 195.5)

        self.metals=[silver, gold, iron]
