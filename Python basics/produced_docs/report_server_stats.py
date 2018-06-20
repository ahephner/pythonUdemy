import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

file = r"C:\Users\AJ Hephner\Documents\GP\stats.xlsx"
writer = pd.ExcelWriter(r"C:\Users\AJ Hephner\Documents\GP\cleanstat.xlsx", engine='xlsxwriter')

#import data files
day = pd.read_excel(file, sheet_name='Reports_24')
week = pd.read_excel(file, sheet_name='Reports_Week')
user = pd.read_excel(file, sheet_name='Usage_By_User')
times_run = pd.read_excel(file, sheet_name='Reports_Times_Run')
data_source = pd.read_excel(file, sheet_name='Reports_Data_Source')

#sort values
day_sort = day.sort_values(by='TimesRun', ascending= False)
week_sort = week.sort_values(by= 'TimesRun', ascending = False)
user_sort = user.sort_values(by= 'TimesRun', ascending = False)
times_run_sort = times_run.sort_values(by = 'TimesRun', ascending = False)
#group by                                              .size() needs called 
data_source_sort = data_source.groupby(['DataSources']).size()


#put sorted data into a dictonary to send to excel
frames = {'24hours': day_sort, 'Week': week_sort, 'TimesRun': times_run_sort, 'DataSource': data_source_sort} 


#send to excel by looping through frames dict
for sheet, frame in frames.items():
    frame.to_excel(writer, sheet_name = sheet)

writer.save()
