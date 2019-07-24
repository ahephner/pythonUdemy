import pandas as pd
import datetime

df = pd.read_excel(r"C:\Users\AJ Hephner\Desktop\aug-nov 18 ar.xlsx" )
print(df.head(1))

#Clean here 
##Cedit Memo's should be split out to df
##Returns need to be negative, also split those out to another df while keeping in original

returns = df[df['RM_Doc_Type']=='Return']
credit_df = df[df['RM_Doc_Type']=='Credit Memo']
df = df[df['RM_Doc_Type']!= 'Credit Memo']

df['GL_Posting_Date'] = df['GL_Posting_Date'].dt.strftime('%B') 
df = df.groupby('GL_Posting_Date').sum().reset_index()
df.head()

returns['GL_Posting_Date'] = returns['GL_Posting_Date'].dt.strftime('%B') 
returns = returns.groupby('GL_Posting_Date').sum().reset_index()
r = returns.copy()
r.iloc[:,1:] = r.iloc[:,1:].mul(-1)

final=df.copy()
final['Original_Trx_Amount'] = df['Original_Trx_Amount']+ r['Original_Trx_Amount']
final['Current_Trx_Amount'] = df['Current_Trx_Amount'] + r['Current_Trx_Amount']
final['Total_Applied_Amount'] = df['Total_Applied_Amount'] + r['Total_Applied_Amount']
final['Amount_Applied'] = df['Amount_Applied'] + r['Amount_Applied']
final['Discount'] = df['Discount'] + r['Discount']
final['Writeoff'] = df['Writeoff'] + r['Writeoff']
final['Applied_To_Doc_Total'] = df['Applied_To_Doc_Total'] + r['Applied_To_Doc_Total']
final['Applied_To_Doc_Unapplied_Amount'] = df['Applied_To_Doc_Unapplied_Amount'] + r['Applied_To_Doc_Unapplied_Amount']

final.to_csv(r"C:\Users\AJ Hephner\Downloads\report1563968449250.csv", index=False)
