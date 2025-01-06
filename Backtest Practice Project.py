import Backtest_Practice_Project_Functions as btf
import Simple_Strategy as st


dollars = float(input('What is your starting amount: '))
current_position = 0 
shares = 0 

data = btf.opencsv()
(date, openprice, closeprice) = data

i = 5
while i<len(date) - 5:
    condition = st.strategy(closeprice, current_position, i)
    
    price = closeprice[i]
    (dollars, shares, current_position) = btf.trading_account(dollars,shares,condition,price)
    i+=1 

if shares > 0:
    dollars = btf.shares_to_dollars
    shares = 0 
print(dollars)


