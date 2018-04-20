import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



#excel example
file = r"C:\Users\ajhep\Desktop\python.xlsx"
csv = r"C:\Users\ajhep\Desktop\csv.csv" 


df = pd.read_excel(file, index_col = 0)
    
print(df.head())  
print(df.shape)

#describe gives stats for each column
print(df.describe())

#sort by weight

heavy = df.sort_values(['WEIGHT'], ascending = False)




heavy.head(10).plot(kind='barh')
plt.show()

# data = np.recfromcsv(csv, usecols =[4])
# print(data)


