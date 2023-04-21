# The code below is used to extract data from an excel sheet
import pandas as pd
from IPython.display import display

df = pd.read_excel('energy market.xlsx')

def purchase(energy_amt, energy_type):
    new_limit = df['Sales Limit'][energy_type] - energy_amt
    df['Sales Limit'][energy_type] = new_limit
    df.to_excel('energy market.xlsx')

purchase(25, 0)

#display(df['Sales Limit'][0])

display(df)
