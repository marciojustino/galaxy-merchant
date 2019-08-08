
class RomanNumber {

    constructor(symbol, value, isRepeatable) {
        this.symbol = symbol;
        this.value = value;
        this.isRepeatable = isRepeatable;
        this.subtracts = [];
    }

    addSubtracts(romanNumbers) {
        romanNumbers.forEach(n => this.subtracts.push(n));
    }
}

module.exports = RomanNumber;