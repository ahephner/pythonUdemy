import pandas as pd
sales = pd.read_csv(rSALESCSVHERE)
reps = pd.read_csv(REPIDCSVHERE)

#group by product order by qty
byproduct = sale.groupby(['Name', 'Product Name','Product: Product #']).sum().reset_index()
dfqty  = byproduct.groupby(["Name"]).apply(lambda x: x.sort_values(["Qty"], ascending = False)).reset_index(drop=True)

#want only top 15 products if you want more or less change amount here
dfqty = dfqty.groupby('Name').head(15)
print(dfqty.head(45))

#make a copy and merge rep id's then set col headers for dataloader upload
df = dfqty.copy()
df = df.merge(rep, on='Name', how='right')

#don't want house values reps only
df = df[~df['Name'].str.contains('House')]
df['Start Date'] = '8/1/2020'
df['End Date'] = '9/30/2020'
df['Goal Name'] = df['Name'] +' '+ df['Product Name'] + " Aug/Sept '20 "
df['Budget Type'] = 'Total Sales'
df['Forecast Amount'] = 0
df['Forcecast Qty'] = 0
df['Product Forecast?'] = True

#get cols we need 
df = df[['Product: Product #', 'Extended Price', 'Qty', 'Start Date', 'End Date', 'Id', 'Goal Name', 'Budget Type', 'Forecast Amount', 'Forcecast Qty','Product Forecast?']]

#bye
df.to_csv(r'C:\Users\AJ Hephner\Desktop\python landings\testcoll.csv',index=False)
