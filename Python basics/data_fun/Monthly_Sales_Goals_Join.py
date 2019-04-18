import pandas as pd
#files
febg = r"C:\Users\AJ Hephner\Documents\2019\Work Bench\feb goals.csv"
feba = r"C:\Users\AJ Hephner\Documents\2019\Work Bench\feb act.csv"
marg = r"C:\Users\AJ Hephner\Documents\2019\Work Bench\march goals.csv"
mara = r"C:\Users\AJ Hephner\Documents\2019\Work Bench\march act.csv"
rid = r"C:\Users\AJ Hephner\Documents\2019\Work Bench\reps_id.csv"

#load files 
fg = pd.read_csv(febg)
fa = pd.read_csv(feba)
mg = pd.read_csv(marg)
ma = pd.read_csv(mara)
rep = pd.read_csv(rid)

#find rep col headers rename to match
rep.head()
rep = rep.rename(columns={'Id': 'Sales_Rep__c'})
rep.info()

#merge reps on sales goals 
fg = pd.merge(fg, rep, on='Sales_Rep__c',  how='outer')
fg.head()
#merge goals and sales 
fa = pd.merge(fa, fg, on ='Name_y', how= 'outer')
fa.head(3)

#repeat of above 
mg = pd.merge(mg, rep, on='Sales_Rep__c',  how='outer')

ma = ma.rename(columns={'Sales Rep': 'Name_y'})
mg.head(2)

ma = pd.merge(ma, mg, on ='Name_y', how= 'outer')
ma.head(2)

march_final = ma[['Id','Progress Amount']]
march_final.head()

feb_final = fa[['Id', 'Progress Amount']]
feb_final.head(2)

#combine df
final = pd.concat([feb_final, march_final],ignore_index=True,  sort=False)

#drop reps without goals 
test = final.dropna()

#bye
test.to_csv(r"C:\Users\AJ Hephner\Documents\2019\Work Bench\update.csv", index=False)
