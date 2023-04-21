# The code below is used to extract data from an excel sheet
import pandas as pd
from IPython.display import display

df = pd.read_excel('energy market.xlsx')

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




purchase(25, 1)
sell(25, 1)

#display(df['Sales Limit'][0])

display(df)
