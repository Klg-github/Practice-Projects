import csv


def opencsv():
    filename = input('Filename: ')
    with open(f'{filename}') as csvfile:
        reader = csv.DictReader(csvfile)

        date = []; openprice = []; closeprice = []
        for row in reader:
            date.append(row['Date'])
            openprice.append(float(row['Open'].replace(',','')))
            closeprice.append(float(row['Close'].replace(',','')))

    return date, openprice, closeprice


def dollar_to_shares(dollars, price):
        return dollars / price

def shares_to_dollars(shares, price):
     return shares*price

def trading_account(dollars, shares, condition, price):
    if condition == 0: #Hold
        current_position = 1
        return dollars, shares, current_position
    elif condition == 3: #Hold
         current_position = 0
         return dollars, shares, current_position
    elif condition == 1: #Buy
       shares = dollar_to_shares(dollars, price)  
       dollars = 0
       current_position = 1 
       return dollars, shares, current_position
    elif condition == 2: #Sell
        dollars = shares_to_dollars(shares, price)
        shares = 0 
        current_position = 0
        return dollars,shares, current_position





