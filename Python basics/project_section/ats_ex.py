import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

file = r"C:\Users\ajhep\Desktop\Sales Goal Insert_error.csv"

open = pd.read_csv(file, index_col='Sales Rep Name')


print(open.head())

open.reset_index(inplace=True)

open.head()

#grab kevin cust
kw = (open['Sales Rep Name']=='Kevin Wolfe')

#grab all the indexs i need
kw = open.loc[(open['Sales Rep Name']=='Kevin Wolfe'), ['Customer Name', 'Budget', 'Forecast', ]]

print(kw.describe())

#save large end-user
budget = kw.loc[(kw['Budget'] > 70000)]




