from src.galaxy_merchant_transaction import GalaxyMerchantTransaction
from src.galaxy_merchant_exception import GalaxyMerchantException
import re
import os


class GalaxyMerchant:
    outputFilePath = 'output'
    outputFileName = 'results.txt'

    def __init__(self):
        super().__init__()
        self.file = None

    def __create_output_file(self):
        try:
            if not os.path.exists(self.outputFilePath):
                os.mkdir(self.outputFilePath)
            self.file = open('{}/{}'.format(self.outputFilePath, self.outputFileName), 'w+')
        except IOError as error:
            print("Can't create output file. Error={}".format(error))
        except:
            print('Error on create output file.')

    def __close_output_file(self):
        try:
            self.file.close()
        except:
            return

    def process_transactions(self, transactions):
        try:
            results = []
            gmt = GalaxyMerchantTransaction()
            self.__create_output_file()
            for t in transactions:
                try:
                    terms = re.split(r'\s+', t)
                    result = gmt.process(terms)
                    if result:
                        self.file.write('{}\n'.format(result))
                        results.append(result)
                except GalaxyMerchantException as error:
                    self.file.write('{}\n'.format(error))
                    results.append(error)
            return results
        finally:
            self.__close_output_file()