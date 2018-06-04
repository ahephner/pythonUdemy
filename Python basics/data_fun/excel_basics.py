import pandas as pd 
from datetime import datetime 
import xlsxwriter 

#create workbook and add two worksheets 
workbook = xlsxwriter.Workbook(r'C:\Users\ajhep\Desktop\excel_py.xlsx')
worksheet_one = workbook.add_worksheet('test')
worksheet_two = workbook.add_worksheet('test2')


#data
data = (
    ['Miles Ran','2018-06-04', 8],
    ['Miles Ran','2018-06-05', 7],
    ['Miles Ran','2018-06-06', 7],
    ['Miles Ran','2018-06-07', 7]
)

#add bold format
bold = workbook.add_format({'bold': True})

#add date format

date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

#add col headers
worksheet_one.write('B1', 'Date', bold)
worksheet_one.write('C1', 'Miles', bold)
#col and row start rows and columns are zero index
row = 1
col = 0 


for i,t,  c in (data):
    # Convert the date string into a datetime object.
    date = datetime.strptime(t, "%Y-%m-%d")
    
    worksheet_one.write_string (row, col, i)
    worksheet_one.write (row, col+1, t, date_format)
    worksheet_one.write_number (row, col +2, c)
    row += 1

worksheet_one.write(row, 0, 'Total', bold) 
worksheet_one.write(row, 2, '=SUM(C2:C4)')

workbook.close()