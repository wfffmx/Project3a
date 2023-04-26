import csv 

def sp500_symbols():
    symbols = [] #Creates an array of symbols

    with open('S&P.csv', 'r') as csvfile:
        Stocks_reader = csv.reader(csvfile)
        for row in Stocks_reader:
            symbols.append(row[0])

    return symbols