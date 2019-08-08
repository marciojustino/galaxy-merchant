const RomanNumeral = require('./roman-number');
const GalacticNumeral = require('./galactic-numeral');

class GalaxyMerchant {

    constructor() {
        this.constructRomanNumbers();
        this.constructGalacticRomanRelation();
    }

    constructRomanNumbers() {
        this.romanNumeralI = new RomanNumeral('I', 1, true);
        this.romanNumeralV = new RomanNumeral('V', 5, false);
        this.romanNumeralX = new RomanNumeral('X', 10, true);
        this.romanNumeralL = new RomanNumeral('L', 50, false);
        this.romanNumeralC = new RomanNumeral('C', 100, true);
        this.romanNumeralD = new RomanNumeral('D', 500, false);
        this.romanNumeralM = new RomanNumeral('M', 1000, true);

        this.romanNumeralI.addSubtract([this.romanNumeralV, this.romanNumeralX]);
        this.romanNumeralX.addSubtract([this.romanNumeralL, this.romanNumeralC]);
        this.romanNumeralC.addSubtract([this.romanNumeralD, this.romanNumeralM]);
    }

    constructGalacticRomanRelation() {
        this.glob = new GalacticNumeral('glob', this.romanNumeralI);
        this.prok = new GalacticNumeral('prok', this.romanNumeralV);
        this.pish = new GalacticNumeral('pish', this.romanNumeralX);
        this.tegj = new GalacticNumeral('tegj', this.romanNumeralL);
    }

    constructMetal() {
        this.metalSilver = new Metal('Silver', 32);
        this.metalGold = new Metal('Gold', 57794);
        this.metalIron = new Metal('Iron', 3890);
    }

    extractMerchantTransaction(merchantTransaction) {
        return merchantTransaction.split(' ');
    }

    negotiate(merchantTransaction) {
        let inputItems = this.extractMerchantTransaction(merchantTransaction);

        //todo: extract galactic

        //todo: extract metal items

        //todo: validate subtracted elements
    }
}