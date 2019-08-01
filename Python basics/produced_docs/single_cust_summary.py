import pandas as pd
import datetime

df = pd.read_excel(r"C:\Users\AJ Hephner\Documents\2019\A&R\jun1_18_july30_19.xlsx")

print(df.head(2))

cust = df[df['CUSTNMBR']==100119]
print(cust)

cust.to_excel(r"C:\Users\AJ Hephner\Downloads\My Sales Analysis By Customer-2019-07-30-11-54-47.xlsx")
returns = cust[cust['RM_Doc_Type']=='Return']
credit = cust[cust['RM_Doc_Type']=='Credit Memo']
no_c_r = cust[(cust['RM_Doc_Type']!='Return')&(cust['RM_Doc_Type']!='Credit Memo')] 
no_c_r['Document_Date'] = no_c_r['Document_Date'].dt.strftime('%B')

print(no_c_r.head(1))

no_c_r = no_c_r.groupby('Document_Date').sum().reset_index()
no_c_r.to_excel(r"C:\Users\AJ Hephner\Downloads\My Sales Analysis By Customer-2019-07-30-11-54-47.xlsx", index=False)
returns['Document_Date'] = returns['Document_Date'].dt.strftime('%B')

returns = returns.groupby('Document_Date').sum().reset_index()
returns.to_excel(r"C:\Users\AJ Hephner\Downloads\My Sales Analysis By Customer-2019-07-29-12-38-58.xlsx", index = False)
credit['Document_Date'] = credit['Document_Date'].dt.strftime('%B')
credit = credit.groupby('Document_Date').sum().reset_index()

credit.to_excel(r"C:\Users\AJ Hephner\Downloads\My Sales Analysis By Customer-2019-07-29-12-38-58.xlsx", index = False)
