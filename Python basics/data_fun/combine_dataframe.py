import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

file = r"C:\Users\ajhep\Desktop\Sales Goal LTO.csv"
top = pd.read_csv(file, thousands = ',')

print(top.iloc[3])

#this is the column to add
dif = top['Budget (sg)'] - top['Forecast (gp)']


df = [top, dif]

#blend 
result = pd.concat(df, axis = 1, join= 'inner')

print(result)