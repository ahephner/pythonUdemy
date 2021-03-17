import pandas as pd 
from datetime import datetime, timedelta
#this is all sales i need to change var
sales = pd.read_csv(r'filepath')
reps = pd.read_csv(rfilepath)
#goals combined into one fild
all_goals = pd.read_csv(r'filepath')
#to update dataloader
update = r'filepath'

#print(herb.head(1))
#dates for YOY compare  in sf
x = datetime.now() - timedelta(days=365)
# print('Todays Date a year ago:')
# print(x)

#herb = herb.rename(columns={'Sales Rep (Doc): Sales Rep': 'Sales Rep', 'Extended Price': 'Previous YTD Sales', 'LTO Focus Product Category': 'group'})
sales['Doc Date'] = pd.to_datetime(sales['Doc Date'])
sales = sales[sales['Doc Date']<= x]
# print('after column rename')
# print(herb.head(1))
df = sales.groupby(['LTO Focus Product Category', 'Sales Rep (Doc): Sales Rep']).sum().reset_index()

df['Prev YTD Margin'] = df['Gross Profit'] / df['Extended Price'] * 100

add_rep = reps.merge(df, on='Sales Rep (Doc): Sales Rep')
add_rep = add_rep.rename(columns={'Id': 'Sales Rep', 'Extended Price': 'PREV YTD Sales', 'LTO Focus Product Category': 'group'})

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

# print('after .apply()')
# print(all_goals.head(1))
print(add_rep.head(5))
print(all_goals.head(1))
join = all_goals.merge(add_rep, on =['Sales Rep', 'group'])
# print('after join merger')
# print(join.head(25))

to_sf = join[['Record ID', 'PREV YTD Sales', 'Prev YTD Margin']]

#bye 
to_sf.to_csv(update, index = False)
