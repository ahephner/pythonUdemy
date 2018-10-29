import pandas as pd
import numpy as np
import xlsxwriter

file = (r"C:\Users\AJ Hephner\Desktop\testsplit.xlsx")

x = pd.read_excel(file)

print(x.head())

#Below will split the cell where "-" is
new = x["Account Name"].str.split("-", n=1, expand= True)

#this is where we change the value. I could put anything in I want as long as i bring the same number of rows into the excel sheet. 
new[0] = "2018/19 " + x["Sales_Rep__r.Sales Rep"] + " (" + new[0].astype(str) + ")"

#now we send to excel notice we are only sending the one column not the whole sheet.
new[0].to_excel(r"C:\Users\AJ Hephner\Desktop\aftersplit.xlsx", index = False)
