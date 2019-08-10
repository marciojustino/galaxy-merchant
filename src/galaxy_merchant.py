from src.galaxy_merchant_transaction import GalaxyMerchantTransaction
from src.galaxy_merchant_exception import GalaxyMerchantException
import re


class GalaxyMerchant:
    def __init__(self):
        super().__init__()

    def process_transactions(self, transactions):
        results = []
        gmt = GalaxyMerchantTransaction()
        for t in transactions:
            try:
                terms = re.split(r'\s+', t)
                result = gmt.process(terms)
                if result:
                    results.append(result)
            except GalaxyMerchantException as error:
                results.append(error)
        return results
