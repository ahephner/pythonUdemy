import pandas as pd
#dataloader sales, goals, rep get id's for them all crucial to joins

sales = pd.read_csv()
goals = pd.read_csv()
rep = pd.read_csv()

sales.head()

sales = sales.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep']).sum().reset_index()

rep.head()
sales = sales.rename(columns={'Sales Rep (Doc): Sales Rep': 'Name'})

add_rep = add_rep.rename(columns={'Id': 'Sales_Rep__c', 'Real Account ID': 'Customer__c'})
add_goal = add_rep.merge(goals, on=['Customer__c', 'Sales_Rep__c'], how='outer')
df = add_goal

#because there are sales to accounts without goals we will get a lot of NA values need to drop before trying to upload
df = df.dropna()
#bye
df.to_csv(r"C:\Users\AJ Hephner\Downloads\report1568373490380.csv")
