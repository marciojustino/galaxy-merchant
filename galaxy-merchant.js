const RomanNumeral = require('./roman-number');
const GalacticNumeral = require('./galactic-numeral');
const Metal = require('./metal');
const GalaxyMerchantTransactionError = require('./galaxy-merchant-transaction-error');

class GalaxyMerchant {

    constructor() {
        this.constructRomanNumbers();
        this.constructGalacticsNumbers();
        this.constructMetals();
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

    validateTransaction(merchantTransaction) {
        if (!merchantTransaction) {
            throw new GalaxyMerchantTransactionError();
        }

        const patterns = [
            /^how many Credits is\s/gi,
            /^how much is\s/gi
        ];

        let transactionTerms = undefined;
        patterns.forEach(async (p) => {
            if (merchantTransaction.match(p)) {
                transactionTerms = merchantTransaction.replace(p, '');
            }
        });

        if (!transactionTerms) {
            throw new GalaxyMerchantTransactionError();
        }

        return transactionTerms;
    }

    getTransactionTerms(merchantTransactionOperators) {
        const transactionOperators = merchantTransactionOperators.match(/(\w+\s)+/)[0];
        return transactionOperators.trim().split(/\s/g);
    }

    validateTransactionTerms(transactionTerms) {
        if (!transactionTerms) {
            throw new GalaxyMerchantTransactionError();
        }

        transactionTerms.forEach(term => {
            if (!this.galacticNumerals.filter(g => g.symbol === term) || !this.metals.filter(m => m.symbol === term)) {
                throw new GalaxyMerchantTransactionError(`Operator ${term} is not valid for galactic transaction`);
            }
        });
    }

    extractGalacticTerms(transactionTerms) {
        let t_galacticNumbers = [];
        transactionTerms.forEach(term => {
            t_galacticNumbers.push(this.galacticNumerals.filter(galacticNumber => {
                return galacticNumber.symbol === term
            }));
        });

        return t_galacticNumbers;
    }

    processTransaction(merchantTransaction) {
        let merchantTransactionOperators = this.validateTransaction(merchantTransaction);
        let transactionTerms = this.getTransactionTerms(merchantTransactionOperators);
        this.validateTransactionTerms(transactionTerms);

        //todo: extract galactic
        let galacticTerms = this.extractGalacticTerms(transactionTerms);

        console.log(galacticTerms);

        //todo: extract metal items

        //todo: validate subtracted elements
    }
}

module.exports = GalaxyMerchant;