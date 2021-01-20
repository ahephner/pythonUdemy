import pandas as pd 
#run https://advancedturf.lightning.force.com/lightning/r/Report/00O2M000008zoVlUAI/view?queryScope=userFolders to get sales #
#export as csv.....
sales = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2020\Golf Focus Product\allLastYearSaleswNewProducts.csv")
reps = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\Work Bench\reps_id.csv')
goals = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2020\Golf Focus Product\salesgoals.csv')
land = r"C:\Users\AJ Hephner\Documents\2020\Golf Focus Product\After Morgan Updates.csv"

df = sales.groupby(['Golf Focus Product Category', 'Sales Rep (Doc): Sales Rep']).sum().reset_index()
df['Progress Margin'] = df['Gross Profit']/df['Extended Price'] * 100

reps = reps.rename(columns={'Name': 'Sales Rep (Doc): Sales Rep'})

add_rep = reps.merge(df, on='Sales Rep (Doc): Sales Rep')
print('add rep merg')
print(add_rep)
add_rep = add_rep.rename(columns={'Id': 'Sales Rep', 'Extended Price': 'Progress Amount'})

goals = goals.rename(columns={'Focus Product Category': 'FP'})
def gp(fp):
    if fp == '28/44/Gold (Golf)':
        fp = '28/44/Gold (Golf)<br>'
    elif fp == 'Bentgrass': 
        fp = 'Bentgrass<br>'
    elif fp == 'Foliar-Pak':
        fp = 'Foliar-Pak + PB1<br>'
    elif fp == 'TMI/ZOXY/Rotator (Golf)':
        fp = 'TMI/ZOXY/Rotator (Golf)<br>'
        
    return fp 
goals['Golf Focus Product Category'] = goals.FP.apply(gp)
print('goals')
print(goals)
join = goals.merge(add_rep, on=['Sales Rep', 'Golf Focus Product Category'])

print(join.tail(15))


to_sf = join[['Record ID', 'Sales Rep', 'Progress Margin', 'Progress Amount']]
print('total ')
print(sum(to_sf['Progress Margin']))

to_sf.to_csv(land, index = False)

