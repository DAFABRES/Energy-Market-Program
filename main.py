# This code is an implementation of an energy market where users can buy and sell solar and wind energy. 
# The data is stored in an Excel file and the program uses the Pandas library to read and write to it. 
# The market can be opened and closed, and users can buy and sell energy within certain limits. 
# There is also a transaction history that is stored in a separate DataFrame.

import pandas as pd
def login():
    # Ask for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if username and password match
    if username == "OSI" and password == "password":
        print("Login successful!")
    else:
        print("Incorrect username or password. Please try again.")

########################################################################
def open_market():
    # Load the initial market data from the Excel file
    #df = pd.read_excel('energy market.xlsx', sheet_name='Sheet1')
    df["Daily Limit"][0] = 100
    # Update the available energy and sales limit columns in the main dataframe with the initial values
    for i, row in df.iterrows():
        energy_type = row['Energy Type']
        df.loc[df['Energy Type'] == energy_type, 'Available Energy'] = row['Available Energy']
        df.loc[df['Energy Type'] == energy_type, 'Sales Limit'] = row['Sales Limit']
    
    # Write the updated dataframe to the Excel file with a new sheet name indicating the market is open again
    with pd.ExcelWriter('energy market.xlsx', engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name='Open Market', index=False)
    
    print("Market opened")

########################################################################

def close_market():
    # Write the current dataframe to the Excel file with a new sheet name indicating the market is closed
    with pd.ExcelWriter('energy market.xlsx', engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name='Closed Market', index=False)
    
    print("Market closed")

########################################################################
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

########################################################################
def sell(energy_amt, energy_type):
    if df['Available Energy'][energy_type] < df['Sales Limit'][energy_type]:
        df['Sales Limit'][energy_type] = df['Sales Limit'][energy_type] + energy_amt  #adds to sales limit
        df["Available Energy"][energy_type] = df["Available Energy"][energy_type] - energy_amt #takes from our storage
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

########################################################################
#should check if trade is possible, needs work
def trade(energy_amt, action: str, choice):
    if (df["Daily Limit"][0] - energy_amt) < 0: 
        print("You have reached the trading limit of 100kw per tariff due to FERC limitations.")
    else:
        if action == 'buy':
            purchase(int(energy_amt), choice)
        else:
            sell(int(energy_amt), choice)

########################################################################

login()

df = pd.read_excel('energy market.xlsx')    #Reads excel file 
transaction_history = pd.DataFrame(columns=['Transaction Type', 'Energy Type', 'Units'])    #makes dataframe for transaction history
open_market()   #

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
        i = i + 1
print(transaction_history)
close_market()