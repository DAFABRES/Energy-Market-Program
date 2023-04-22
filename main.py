# The code below is used to extract data from an excel sheet
import pandas as pd

df = pd.read_excel('energy market.xlsx')
transaction_history = pd.DataFrame(columns=['Transaction Type', 'Energy Type', 'Units'])


def purchase(energy_amt, energy_type):
    if df['Available Energy'][energy_type] > 0:
        df['Sales Limit'][energy_type] = df['Sales Limit'][energy_type] - energy_amt #takes from sales limit
        df["Available Energy"][energy_type] =  df["Available Energy"][energy_type] + energy_amt # adds to our storage
        df["Money"][0] = df["Money"][0] - (df['Price per unit (kwh)'][energy_type] * energy_amt) #money counter
        df['Daily Limit'][0] =  df['Daily Limit'][0] - energy_amt #daily counter
        
        # add transaction details to transaction_history DataFrame
        transaction_history.loc[len(transaction_history)] = ['Purchase', df['Energy Type'][energy_type], energy_amt]

        # write both DataFrames to the excel file
        with pd.ExcelWriter('energy market.xlsx') as writer:
            df.to_excel(writer, sheet_name='Energy Market', index=False)
            transaction_history.to_excel(writer, sheet_name='Transaction History', index=False)
        df.to_excel('energy market.xlsx', index=False)

    else:
        print("unable to purchase")

def sell(energy_amt, energy_type):
    if df['Available Energy'][energy_type] < df['Sales Limit'][energy_type]:
        df['Available Energy'][energy_type] = df['Available Energy'][energy_type] + energy_amt  #adds to sales limit
        df["Available Energy"][energy_type] = df["Available Energy"][energy_type] - energy_type #takes from our storage
        df["Money"][0] = df["Money"][0] + (df['Price per unit (kwh)'][energy_type] * energy_amt) #money counter
        df['Daily Limit'][0] =  df['Daily Limit'][0] - energy_amt  #daily counter
        
        # add transaction details to transaction_history DataFrame
        transaction_history.loc[len(transaction_history)] = ['Sell', df['Energy Type'][energy_type], energy_amt]

         # write both DataFrames to the excel file
        with pd.ExcelWriter('energy market.xlsx') as writer:
            df.to_excel(writer, sheet_name='Energy Market', index=False)
            transaction_history.to_excel(writer, sheet_name='Transaction History', index=False)
        df.to_excel('energy market.xlsx', index=False)
    else:
        print("unable to purchase")

#should check if trade is possible, needs work
def trade(energy_amt, action: str, choice):
    if (df["Daily Limit"][0] - energy_amt) < 0: 
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
        trade(int(amount),action, choice)
        print(df)
    elif action == "sell":
        print(df)
        energy = input("which energy would you like to sell?")
        if energy == "solar":
            choice = 0
        elif energy == "wind":
            choice = 1
        else:
            print("invalid input")
        amount = input("How much would you like to sell?")
        #def here to check if limit is reached
        trade(int(amount),action, choice)
        print(df)
    elif action == "quit":
        print(transaction_history)
        i = i + 1