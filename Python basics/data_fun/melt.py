# melt is a pandas function that pivots table data from wide
# to long 
# example before
# 123
# after
# 1
# 2
# 3

import pandas as pd 


df = pd.read_excel(r"C:\Users\ajhep\Desktop\python.xlsx")

# There are two parameters you should be aware of: id_vars and value_vars. 
# The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape) 
# the value_vars represent the columns you do wish to melt into rows. 
# By default, if no value_vars are provided, all columns not set in the id_vars will be melted. 

football_melt = pd.melt(df, id_vars='PLAYER')

print(football_melt.head())


name_col = pd.melt(df, id_vars= ['PLAYER','Fname'], var_name ='postion', value_name = 'F')
print(name_col.head())