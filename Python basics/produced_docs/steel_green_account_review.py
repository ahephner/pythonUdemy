import pandas as pd 
#import files
before = pd.read_excel()
after = pd.read_excel()
info = pd.read_excel()
b = before.dropna()
a = after.dropna()

both = b.merge(a, on = ['Real Id', 'Sales Rep'], how="left")
both = both.rename(columns={'Account_x': 'Account'})
both = both.fillna(0)

both.head(1)

both = both[['Sales Rep', 'Account', 'Real Id', 'Before Sales', 'Before Margin', 'After Sales', 'After Margin']]
#get only sales after accounts
ona = b.merge(a, on = ['Real Id', 'Sales Rep'], how="right", indicator=True)
ona = ona[(ona['After Sales']>=0) & (ona['_merge'].str.contains('right_only'))]
ona = ona[['Sales Rep', 'Real Id', 'Before Sales', 'Before Margin', 'Account_y', 'After Sales', 'After Margin']]

ona = ona.fillna(0)
ona = ona.rename(columns={"Account_y": "Account"})  

#join df's together
all = both.append(ona)
all = all.merge(info, on='Real Id', how="right", indicator=True)
#get no sales other than units
uo = all[all["_merge"].str.contains('right')]
#get accounts that have purchased other goods 
all = all[all['_merge'].str.contains('both')]


#get cols for df
print(all.head(1))
all = all[['Account', 'After Margin', 'After Sales', 'Before Margin', 'Before Sales', 'Real Id', 'Sales Rep_x', 'Steel Green Purchase Date', 'Number of Units Purchased']]
all = all.rename(columns={'Sales Rep_x': 'Sales Rep'})
print(all.head(1))
print(all.tail())

uo = uo[['Real Id', 'Sales Rep_y', 'Account_y', 'Steel Green Purchase Date', 'Number of Units Purchased']]
uo['After Margin'] = 0
uo['After Sales'] = 0
uo['Before Margin'] = 0
uo['Before Sales'] = 0
#join
final = all.append(uo)

final = final.sort_values('Sales Rep')
no = final[final['After Sales'] <= 0]
low = final[(final['After Sales'] <= 1000) & (final['After Sales']>0)]
noBefore = all[all['Before Sales']<= 100]

#out
no.to_excel(r"C:\Users\AJ Hephner\Downloads\ATS Accounts at GIE-2020-02-26-11-34-06.xlsx", index=False)
