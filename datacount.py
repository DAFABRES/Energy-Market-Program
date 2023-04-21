# Keeping track of the names of the energy that were bought or sold.

import pandas as pd
from IPython.display import display

df = pd.read_excel('energy market.xlsx')

# create an empty DataFrame for transaction history
transaction_history = pd.DataFrame(columns=['Transaction Type', 'Energy Type', 'Units'])

def purchase(energy_amt, energy_type):
    if df['Available Energy'][energy_type] > 0:
        new_limit = df['Available Energy'][energy_type] - energy_amt
        df['Available Energy'][energy_type] = new_limit
        
        # add transaction details to transaction_history DataFrame
        transaction_history.loc[len(transaction_history)] = ['Purchase', df['Energy Type'][energy_type], energy_amt]
        
        # write both DataFrames to the excel file
        with pd.ExcelWriter('energy market.xlsx') as writer:
            df.to_excel(writer, sheet_name='Energy Market', index=False)
            transaction_history.to_excel(writer, sheet_name='Transaction History', index=False)
    else:
        print("unable to purchase")

def sell(energy_amt, energy_type):
    if df['Available Energy'][energy_type] < df['Sales Limit'][energy_type]:
        new_limit = df['Available Energy'][energy_type] + energy_amt
        df['Available Energy'][energy_type] = new_limit
        
        # add transaction details to transaction_history DataFrame
        transaction_history.loc[len(transaction_history)] = ['Sell', df['Energy Type'][energy_type], energy_amt]
        
        # write both DataFrames to the excel file
        with pd.ExcelWriter('energy market.xlsx') as writer:
            df.to_excel(writer, sheet_name='Energy Market', index=False)
            transaction_history.to_excel(writer, sheet_name='Transaction History', index=False)
    else:
        print("unable to sell")

# make a sample purchase and sell
purchase(25, 0)
sell(25, 1)

# display the transaction history
display(transaction_history)