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

i = 0
choice = 0
while i < 1:
    action = input("Would you like to buy, sell or quit?")
    if action == "buy":
        energy = input("which energy would you like to buy?")
        if energy == "solar":
            choice = 0
        elif energy == "wind":
            choice = 1
        else:
            print("invalid input")
        amount = input("How much would you like to buy?")
        purchase(int(amount), choice)
        display(df)
    elif action == "sell":
        energy = input("which energy would you like to sell?")
        if energy == "solar":
            choice = 0
        elif energy == "wind":
            choice = 1
        else:
            print("invalid input")
        amount = input("How much would you like to sell?")
        sell(int(amount), choice)
        display(df)
    elif action == "quit":
        i = i + 1
        display(df)

#purchase(25, 1)
#sell(25, 1)

#display(df['Sales Limit'][0])

#display(df)
