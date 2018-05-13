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

# Data Camp

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
#read excel file skip rows columns change column names
# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
