# The code below is used to extract data from an excel sheet
import pandas as pd
from IPython.display import display

df = pd.read_excel('energy market.xlsx')

display(df)

