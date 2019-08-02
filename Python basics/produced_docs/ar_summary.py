import pandas as pd 
import datetime

df = pd.read_excel(r"file")
df.head(1)

returns = df[df['RM_Doc_Type'] == 'Return']
credit_df = df[df['RM_Doc_Type'] == 'Credit Memo']

#remove returns and credit
ncr = df[(df['RM_Doc_Type']!= 'Credit Memo') & (df['RM_Doc_Type']!= 'Return')]

#make sure the removals are correct
returns.describe()
credit_df.describe()
ncr.describe()

#set month
ncr['Document_Date'] = ncr['Document_Date'].dt.strftime('%B') 
ncr = ncr.groupby('Document_Date').sum().reset_index()
ncr.head()
ncr.to_excel(r"C:\Users\AJ Hephner\Documents\2019\A&R\June - Nov 18.xlsx", index=False)

returns['Document_Date'] = returns['Document_Date'].dt.strftime('%B') 
returns = returns.groupby('Document_Date').sum().reset_index()
returns.to_excel(r"C:\Users\AJ Hephner\Documents\2019\A&R\June - Nov 18.xlsx", index=False)

credit_df['Document_Date'] = credit_df['Document_Date'].dt.strftime('%B') 
credit_df = credit_df.groupby('Document_Date').sum().reset_index()
credit_df.to_excel(r"C:\Users\AJ Hephner\Documents\2019\A&R\June - Nov 18.xlsx", index=False)
