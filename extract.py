# The code below is used to extract data from an excel sheet
import pandas as pd
from IPython.display import display

df = pd.read_excel('energy market.xlsx')


def open_market():
    # Load the initial market data from the Excel file
    df_initial = pd.read_excel('energy market.xlsx', sheet_name='Sheet1')
    
    # Update the available energy and sales limit columns in the main dataframe with the initial values
    for i, row in df_initial.iterrows():
        energy_type = row['Energy Type']
        df.loc[df['Energy Type'] == energy_type, 'Available Energy'] = row['Available Energy']
        df.loc[df['Energy Type'] == energy_type, 'Sales Limit'] = row['Sales Limit']
    
    # Write the updated dataframe to the Excel file with a new sheet name indicating the market is open again
    with pd.ExcelWriter('energy market.xlsx', engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name='Open Market', index=False)
    
    print("Market opened")


def purchase(energy_amt, energy_type):
    if df['Available Energy'][energy_type] > 0:
        new_limit = df['Available Energy'][energy_type] - energy_amt
        df['Available Energy'][energy_type] = new_limit
        df.to_excel('energy market.xlsx', index=False)
    else:
        print("unable to purchase")

def sell(energy_amt, energy_type):
    if df['Available Energy'][energy_type] < df['Sales Limit'][energy_type]:
        new_limit = df['Available Energy'][energy_type] + energy_amt
        df['Available Energy'][energy_type] = new_limit
        df.to_excel('energy market.xlsx', index=False)
    else:
        print("unable to purchase")



def close_market():
    # Write the current dataframe to the Excel file with a new sheet name indicating the market is closed
    with pd.ExcelWriter('energy market.xlsx', engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name='Closed Market', index=False)
    
    print("Market closed")


purchase(25, 1)
sell(25, 1)

#display(df['Sales Limit'][0])

display(df)

open_market()

close_market()
