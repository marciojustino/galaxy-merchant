const GalaxyMerchant = require('./galaxy-merchant');

let merchant = new GalaxyMerchant();
const merchantTransactions = [
    'how much is pish tegj glob prok Silver ?'
];

merchantTransactions.forEach(t => {
    try {
        const constants = merchant.processTransaction(t);
        console.log(constants);
    } catch (e) {
        console.error(e.message);
    }
});