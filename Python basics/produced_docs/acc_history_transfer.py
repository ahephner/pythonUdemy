#jnotebook 
import pandas as pd

df = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\transfers.csv')
#drop where no previous rep was there 
df = df.dropna()

df.head(1)

def removeT(string):
    "remove time element from salesforce datetime field"
    return string.split('T')[0].strip()
df.CreatedDate = df.CreatedDate.apply(removeT)

df = df.sort_values('CreatedDate', ascending=False)

#remove names leave only id fields
ids = df[df['NewValue'].map(len)==18]
#here is where I would want to look for a duplicate value for testing
#this dataset duplicate is shown in example 
# qt = ids[ids['AccountId']=='0014100000O8GV6AAN']
# d = qt.drop_duplicates(subset='AccountId', keep='first')
# d
ids = ids.drop_duplicates(subset='AccountId', keep='first')
ids.info()

out = ids.rename(columns={'AccountId': 'Id', 'OldValue': 'Previous_Rep__c', 'CreatedDate': 'Transfer_Date__c'})
#bye
out.to_csv(r'C:\Users\AJ Hephner\Documents\2019\transferLanding.csv', index=False)
