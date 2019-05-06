import pandas as pd

 df = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\lastRun56.csv")
 new = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\test update.csv")
 
 new.head()
 
 new = new.rename(columns={'Customer__c': 'Customer', 'Sales_Rep__c': 'Sales Rep', 'Product_Sub_Total__c': 'Update'})
 
 new = new.groupby(['Customer', 'Sales Rep']).sum().reset_index()
 new.head(2)
 
 df = df.merge(new, on=['Customer', 'Sales Rep'])
 df['New Total'] = df['Update'] + df['Product_Sub_Total__c']
 out = df[df['New Total'] > df['Total Sales']]
 out.info()
 
#here we send out to csv for up loading 
#out.to_csv(some_file)

#Update?
#df['Update'] = df['New Total']
#df['Product_Sub_Total__c'] = df['New Total']
#back to file
