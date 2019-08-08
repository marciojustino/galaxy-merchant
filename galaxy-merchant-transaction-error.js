
/**
 * Galaxy merchant transaction error
 */
class GalaxyMerchantTransactionException extends Error {

    constructor(message = 'I have no idea what you are talking about') {
        super(message);
    }
}

module.exports = GalaxyMerchantTransactionException;