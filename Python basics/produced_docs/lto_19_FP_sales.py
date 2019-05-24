import pandas as pd 
#run https://advancedturf.lightning.force.com/lightning/r/Report/00O2M000008zoFdUAI/view?queryScope=userFolders to get sales #
#export as csv.....
sales = pd.read_csv(r'C:\Users\AJ Hephner\Downloads\report1558614924777.csv')
reps = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\All Customer Goals\Sales Reps Salesforce ID.csv')
goals = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\Goals Upload\LTO\all goals id  fp cat.csv')
land = r'C:\Users\AJ Hephner\Documents\2019\Goals Upload\LTO\Landing Current FY Goals.csv'
df = sales.groupby(['LTO Focus Product Category', 'Sales Rep (Doc): Sales Rep']).sum().reset_index()

df['Progress Margin'] = df['Gross Profit']/df['Extended Price']
add_rep = reps.merge(df, on='Sales Rep (Doc): Sales Rep')

add_rep = add_rep.rename(columns={'Id': 'Sales Rep', 'Extended Price': 'Progress Amount'})

goals = goals.rename(columns={'Focus Product Category': 'FP'})
def gp(fp):
    if fp == 'ENP/Holganix':
        fp = 'ENP (LTO)<br>'
    elif fp == 'Herbicides': 
        fp = 'Herbicides<br>'
    elif fp == 'Precision Labs':
        fp = 'Precision Labs<br>'
        
    return fp 

goals['LTO Focus Product Category'] = goals.FP.apply(gp)

join = goals.merge(add_rep, on=['Sales Rep', 'LTO Focus Product Category'])

#print(join.head(15))

to_sf = join[['Record ID', 'Progress Margin', 'Progress Amount']]
print(to_sf)

#to_sf.to_csv(land, index = False)
