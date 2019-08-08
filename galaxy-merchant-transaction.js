
class GalaxyMerchantTransaction {

    constructor() {
        this.constructRomanNumbers();
        this.constructGalacticsNumbers();
        this.constructMetals();
        this.constructOperators();
    }

    constructRomanNumbers() {
        this.romanNumeralI = new RomanNumeral('I', 1, true);
        this.romanNumeralV = new RomanNumeral('V', 5, false);
        this.romanNumeralX = new RomanNumeral('X', 10, true);
        this.romanNumeralL = new RomanNumeral('L', 50, false);
        this.romanNumeralC = new RomanNumeral('C', 100, true);
        this.romanNumeralD = new RomanNumeral('D', 500, false);
        this.romanNumeralM = new RomanNumeral('M', 1000, true);

        this.romanNumeralI.addSubtracts([this.romanNumeralV, this.romanNumeralX]);
        this.romanNumeralX.addSubtracts([this.romanNumeralL, this.romanNumeralC]);
        this.romanNumeralC.addSubtracts([this.romanNumeralD, this.romanNumeralM]);

        this.romanNumbers = [
            this.romanNumeralI,
            this.romanNumeralV,
            this.romanNumeralX,
            this.romanNumeralL,
            this.romanNumeralC,
            this.romanNumeralD,
            this.romanNumeralM
        ];
    }

    constructGalacticsNumbers() {
        this.glob = new GalacticNumeral('glob', this.romanNumeralI);
        this.prok = new GalacticNumeral('prok', this.romanNumeralV);
        this.pish = new GalacticNumeral('pish', this.romanNumeralX);
        this.tegj = new GalacticNumeral('tegj', this.romanNumeralL);

        this.galacticNumerals = [
            this.glob,
            this.prok,
            this.pish,
            this.tegj
        ];
    }

    constructMetals() {
        this.metalSilver = new Metal('Silver', 32);
        this.metalGold = new Metal('Gold', 57794);
        this.metalIron = new Metal('Iron', 3890);

        this.metals = [
            this.metalSilver,
            this.metalGold,
            this.metalIron
        ];
    }

    constructOperators() {
        this.queryOperators = ['how', 'much', 'many'];
        this.decisionOperators = ['is', 'Credits'];
    }

    isGalactictNumeral(term) {
        return this.galacticNumerals.filter(g => g.symbol === term).length > 0;
    }

    isQueryOperator(term, index) {
        return this.queryOperators.indexOf(term) === index;
    }

    compileTransaction(term, step = 1) {
        switch (step) {
            case 1:
                if (this.isGalactictNumeral(term)) {
                    step = 2;
                }
                break;

            case 2:
                if (this.isGalactictNumeral(term)) {
                    step = 3;
                }
                break;

            case 3:
                if (this.isMetal(term)) {
                    step = 4;
                }
                break;
        }
    }

    processTransaction(sTransaction) {
        let terms = sTransaction.split(/\s/);

        terms.forEach(t => {
            this.compileTransaction(t);
        });
    }
}

module.export = GalaxyMerchantTransaction;