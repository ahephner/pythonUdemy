import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

file = r'C:\Users\ajhep\Desktop\Sales Goal LTO.csv'
sales = pd.read_csv(file, thousands=',')

 #group by function
group = sales.groupby('Focus Products')

 #groupby creates df within a larger df you can itterate over
 #here looking at those inner df key is the name df is the actual data with in the data frame
for key, df in group:
    print(key)
    print(df)

#generator comprehension to return highest inner values from each inner df
#sudo -> sort values in the Budget column in the inner df created on the parent group
#go from highest to lowest slice the top one for key and df in group
top = (df.sort_values(by = 'Budget (sg)', ascending = False)[:1] for key , df in group)


#showing <generator object>
print(type(top))

#empty array to store top
top_seller = pd.DataFrame()

#run generator

for i in top:
    top_seller = top_seller.append(i)

print(top_seller)