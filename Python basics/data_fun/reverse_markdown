import pandas as pd
import numpy as np 

df = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\-S account detail sales 1-1 to 5-21.csv")
reps = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\Sales Reps Salesforce ID.csv")
cust = pd.read_csv(r"C:\Users\AJ Hephner\Documents\JDT\Customer Name, Number, Real Account ID.csv")


df.head(1)
#take out mobilization, contracted, shipping case sens. used .copy because it go rid of key warning
df = df[~df['Product_Name__c'].str.contains('Mobilization')]
df = df[~df['Product_Name__c'].str.contains('Contracted')]
df = df[~df['Product_Name__c'].str.contains('SHIPPING')]

#markeddown reverse
#very similar to sf formula field 
df['md'] = np.where(df['Extended_Price__c']==0, df['Qty__c']*df['Unit_Markdown__c'], df['Extended_Price__c'])

test = df[['Product_Name__c', 'Extended_Price__c','Qty__c','Unit_Markdown__c', 'md']]
test.head()

total = df.groupby(['Customer_Name__c', 'Customer__c']).sum().reset_index()
total.head(10)

#test group by above
#filter_data = df[df['Customer_Name__c'].str.contains('Colts')]
#filter_data['md'].sum()

#see if any empty customer sales 
#zero = total[total['md'] == 0 ]
#print(zero)

#merge customer table
cust_merge = cust.merge(total, on=['Customer_Name__c', 'Customer__c'])

#merge open orders
open = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\ENP\JDT open order 5-21-19.csv")
open = open.rename(columns={"Real Account ID": "Real_Account_ID__c"})

op = open.merge(cust_merge, on = 'Real_Account_ID__c')

#data time 
