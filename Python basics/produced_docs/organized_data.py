import pandas as pd
import xlsxwriter

file = r"C:\Users\AJ Hephner\Documents\Misc. Files\Copy of T&O Expense Workbook 2018.xlsx"

xlsx = pd.ExcelFile(file)

#empty list to unload excel files
xl_sheets = []

#loop through excel file and parse sheet data
for sheet in xlsx.sheet_names:
    xl_sheets.append(xlsx.parse(sheet))

print(xl_sheets)

#combine sheets into 1 dataframe
single = pd.concat(xl_sheets, sort=False)

single.head()

single['Expense Budget']
single['YE 2018']

type(single)

#drop index where name is 
#was NAN NAN 
no_name = single.drop(single.index[[0]])

no_name.head()
