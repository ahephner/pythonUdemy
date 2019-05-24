import pandas as pd 
#run https://advancedturf.lightning.force.com/lightning/r/Report/00O2M000008zoVlUAI/view?queryScope=userFolders #
#export as csv.....
sales = pd.read_csv(r'C:\Users\AJ Hephner\Downloads\report1558702800203.csv')
reps = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\All Customer Goals\Sales Reps Salesforce ID.csv')
goals = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\Goals Upload\Golf 19 Salesgoals ID FP Rep ID.csv')
land = r'C:\Users\AJ Hephner\Documents\2019\Goals Upload\testupload.csv'
df = sales.groupby(['Golf Focus Product Category', 'Sales Rep (Doc): Sales Rep']).sum().reset_index()

df['Progress Margin'] = df['Gross Profit']/df['Extended Price'] * 100
add_rep = reps.merge(df, on='Sales Rep (Doc): Sales Rep')

add_rep = add_rep.rename(columns={'Id': 'Sales Rep', 'Extended Price': 'Progress Amount'})

goals = goals.rename(columns={'Focus Product Category': 'FP'})
def gp(fp):
    if fp == 'AT 28/44':
        fp = 'AT 28/44<br>'
    elif fp == 'Bentgrass': 
        fp = 'Bentgrass<br>'
    elif fp == 'Foliar-Pak':
        fp = 'Foliar-Pak + PB1<br>'
    elif fp == 'Armortech':
        fp = 'Armortech<br>'
        
    return fp 

goals['Golf Focus Product Category'] = goals.FP.apply(gp)

join = goals.merge(add_rep, on=['Sales Rep', 'Golf Focus Product Category'])

print(join.head(15))

to_sf = join[['Record ID', 'Progress Margin', 'Progress Amount']]
# print(to_sf)

to_sf.to_csv(land, index = False)

