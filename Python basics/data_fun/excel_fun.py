import pandas as pd 
import xlrd as xr 
import xlsxwriter  

# file = r"C:\Users\ajhep\Desktop\Copy of Oct-Sept 2018 ForecastMaster(2823).xlsx"

# load = pd.read_excel(file, sheet_name= 'Cagle')

# info = pd.DataFrame(load.iloc[:,0], )

# print(load.iloc[:,0])
# print(load.iloc[:,7])


file = r"C:\Users\ajhep\Desktop\2018 Budget (2).xlsx"
writer = pd.ExcelWriter(r'C:\Users\ajhep\Desktop\2018 Budget.xlsx', engine='xlsxwriter')

load = pd.read_excel(file)
#returns only cols starting with Period
df = [col for col in load if col.startswith('Period')]

#Transpose a sheet 
#cand do load.transpose(args, kwgs)
turn = load.T 
print(turn.head)


# writing to excel 
turn.to_excel(writer, sheet_name = 'Sheet 1')

#clse the writer and output excel 
writer.save()

# worksheet_one = workbook.add_worksheet('test')
# worksheet_two = workbook.add_worksheet('test2')

# worksheet_one.write('A2', 234)

# worksheet_two.write(turn)

# workbook.close()
