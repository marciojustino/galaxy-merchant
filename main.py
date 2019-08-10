from src.galaxy_merchant import GalaxyMerchant
import os

inputFilePath = 'input'
inputFileName = 'input.txt'

input = [
    'glob is I',
    'prok is V',
    'pish is X',
    'tegj is L',
    'glob glob Silver is 34 Credits',
    'glob prok Gold is 57800 Credits',
    'pish pish Iron is 3910 Credits',
    'how much is pish tegj glob glob ?',
    'how many Credits is glob prok Silver ?',
    'how many Credits is glob prok Gold ?',
    'how many Credits is glob prok Iron ?',
    'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'
]

def main():
    try:
        merchant = GalaxyMerchant()
        if not os.path.exists('{}/{}'.format(inputFilePath, inputFileName)):
            print('Input file not exists! Using default input... Path={}/{}'.format(inputFilePath, inputFileName))
        else:
            file = open('{}/{}'.format(inputFilePath, inputFileName), 'r')
            input = [line.replace('\n', '') for line in file.readlines()]
            file.close()
        results = merchant.process_transactions(input)
        for r in results:
            print(r)
    except Exception as error:
        print('Ops! Something is wrong! Error={}'.format(error))

if __name__ == "__main__":
    main()