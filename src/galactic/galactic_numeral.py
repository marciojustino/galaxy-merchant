from src.roman.roman_numeral import RomanNumeral


class GalacticNumeral:
    def __init__(self, symbol, romanNumeral: RomanNumeral):
        self.symbol = symbol
        self.romanNumeral = romanNumeral

    @staticmethod
    def to_string(galactic):
        if not isinstance(galactic, GalacticNumeral):
            raise TypeError()
        return galactic.symbol

    @staticmethod
    def to_roman_string(galactics: list):
        romanSymbols = []
        for g in galactics:
            if not isinstance(g, GalacticNumeral):
                raise TypeError()
            romanSymbols.append(g.romanNumeral.symbol)
        return ''.join(romanSymbols)

    @staticmethod
    def only_symbols(galactics: list):
        symbols = []
        for g in galactics:
            if not isinstance(g, GalacticNumeral):
                raise TypeError()
            symbols.append(g.symbol)
        return ' '.join(symbols)
