import galaxy_merchant_transaction as GalaxyMerchantTransaction


class GalaxyMerchant:
    def __init__(self):
        return super().__init__()

    def process_transaction(self, transaction):
        terms = transaction.split('/\s/')
        galaxyMerchantTransaction = GalaxyMerchantTransaction()
        galaxyMerchantTransaction.process(terms)
