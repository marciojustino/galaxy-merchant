from src.galaxy_merchant_transaction import GalaxyMerchantTransaction
import re

class GalaxyMerchant:
    def __init__(self):
        super().__init__()

    def process_transaction(self, transactions):
        gMT = GalaxyMerchantTransaction()
        for t in transactions:
            terms = re.split(r'\s+', t)
            gMT.process(terms)
