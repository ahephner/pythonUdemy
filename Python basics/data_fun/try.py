import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

file = r"C:\Users\ajhep\Desktop\Golf Expense workbook.xlsx"
second = r'C:\Users\ajhep\Desktop\Golf Expense workbook.xlsx'
#reads entire file 
read = pd.ExcelFile(file)


#built in function to get sheet names used len(sheet_names) to get the number of worksheets
#returns a [] list 
sheets = read.sheet_names
#set to bring all sheets this returns a list
test = sheets[0:]


#import all of the sheets 
big = pd.read_excel(second, sheet_name = test)

print(big)