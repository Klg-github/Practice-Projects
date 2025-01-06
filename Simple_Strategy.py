import numpy as np

def strategy(closeprice, current_position, i):
    
    closemean = np.mean(closeprice[i-5:i-1])

    if closemean <= closeprice[i]:
        if current_position == 1: #0 doesn't have shares 1 has shares
            return 0 #Hold position
        else:
            return 1 #Buy 
    elif closemean > closeprice[i]:
        if current_position ==1:
            return 2 #Sell
        else:
            return 3 #Hold Position
        
      



    #Strategy: Calculate a mean for the last 5 days, if the close price on the current day is lower than the average then buy, if its 
    #higher then sell.

    