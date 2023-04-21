# The code below is used to extract data from an excel sheet
import pandas as pd

df = pd.read_excel('energy market.xlsx')

def purchase(energy_amt, energy_type):
    if df['Available Energy'][energy_type] > 0:
        new_limit = df['Available Energy'][energy_type] - energy_amt
        df['Available Energy'][energy_type] = new_limit
        new_money = df['Price per unit (kwh)'][energy_type] * energy_type #money counter
        df["Money"][0] = df["Money"][0] - new_money
        new_daily =  df['Daily Limit'][0] - energy_amt #daily counter
        df['Daily Limit'][0] = new_daily 
        df.to_excel('energy market.xlsx', index=False)

    else:
        print("unable to purchase")

def sell(energy_amt, energy_type):
    if df['Available Energy'][energy_type] < df['Sales Limit'][energy_type]:
        new_limit = df['Available Energy'][energy_type] + energy_amt
        df['Available Energy'][energy_type] = new_limit
        new_money = df['Price per unit (kwh)'][energy_type] * energy_type #money counter
        df["Money"][0] = new_money + df["Money"][0]
        new_daily =  df['Daily Limit'][0] - energy_amt  #daily counter
        df['Daily Limit'][0] = new_daily
        df.to_excel('energy market.xlsx', index=False)
    else:
        print("unable to purchase")

def trade(energy_amt, action: str, choice):
    if (df['Daily Limit'][0] - energy_amt == 0):
        print("You have reached the daily limit of 100kw per day due to FERC limitations, you can continue trading the next market cylcle")
    else:
        if action == 'buy':
            purchase(int(energy_amt), choice)
        else:
            sell(int(energy_amt), choice)


i = 0
choice = 0
while i < 1:
    action = input("Would you like to buy, sell or quit?")
    if action == "buy":
        print(df)
        energy = input("which energy would you like to buy?")
        if energy == "solar":
            choice = 0
        elif energy == "wind":
            choice = 1
        else:
            print("invalid input")
        amount = input("How much would you like to buy?")
        #def here to check if limit is reached 
        trade(amount,action, choice)
        #purchase(int(amount), choice)
        print(df)
    elif action == "sell":
        energy = input("which energy would you like to sell?")
        if energy == "solar":
            choice = 0
        elif energy == "wind":
            choice = 1
        else:
            print("invalid input")
        amount = input("How much would you like to sell?")
        #def here to check if limit is reached
        trade(amount,action, choice)
       # sell(int(amount), choice)
        print(df)
    elif action == "quit":
        i = i + 1
        print(df)