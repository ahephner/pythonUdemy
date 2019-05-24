import pandas as pd 
from datetime import datetime, timedelta

herb = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\LTO\Last Year\Herbicide.csv")

#goals combined into one fild
all_goals = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\Goals Upload\LTO\all goals id  fp cat.csv')
#to update dataloader
update = r'C:\Users\AJ Hephner\Documents\2019\Goals Upload\LTO\Last Year\LY Goal Upload.csv'


#dates for YOY compare  in sf
x = datetime.now() - timedelta(days=365)
print(x)

herb = herb.rename(columns={'Sales_Document__r.Sales Rep (Doc)': 'Sales Rep', 'Extended Price': 'Previous YTD Sales', 'LTO Focus Product Category': 'group'})
herb['Doc Date'] = pd.to_datetime(herb['Doc Date'])
herb = herb[herb['Doc Date']<= x]
print(herb)
herb = herb.groupby(['Sales Rep', 'group']).sum().reset_index()
herb = herb.fillna(0)
herb['Prev YTD Margin'] = herb['Gross Profit'] / herb['Previous YTD Sales'] * 100


print(herb.head(1))

all_goals = all_goals.rename(columns={'Focus Product Category': 'FP'})
#method gives key to join on so I don't have to keep load multiple files. 
def gp(fp):
    if fp == 'ENP/Holganix':
        fp = 'ENP (LTO)<br>'
    elif fp == 'Herbicides': 
        fp = 'Herbicides<br>'
    elif fp == 'Precision Labs':
        fp = 'Precision Labs<br>'
        
    return fp 

all_goals['group'] = all_goals.FP.apply(gp)

print(all_goals.head(1))

join = all_goals.merge(herb, on =['Sales Rep', 'group'])

print(join.head(25))

to_sf = join[['Record ID', 'Previous YTD Sales', 'Prev YTD Margin']]
#bye 
to_sf.to_csv(update, index = False)