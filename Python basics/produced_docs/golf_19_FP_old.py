import numpy as np 
import pandas as pd 

#landing pages
csv_foliar = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\landingfoliar.csv"
csv_bent = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\landingbent.csv"
csv_at = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\landingAT.csv"
csv_armor = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\landingarmortech.csv"
today = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\testupload.csv"
#dataloader sales_details this should be the only file where we need to rerun dataloader to update
dl_foliar = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\dataloaderFoliar.csv"
dl_bent = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\dataloaderBentgrass.csv"
dl_at = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\dataloaderAT.csv"
dl_armor = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\dataloaderarmortech.csv"

#goals
foliar = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Goal Foliar.csv"
bent = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Goal Bentgrass.csv"
at = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\goalsAT.csv"
armor = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Goal Armortech.csv"
ag = pd.read_csv(at)

#Foliar update
fs = pd.read_csv(dl_foliar)
fg = pd.read_csv(foliar)
fs = fs.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep'})

#print(fs.tail())
fs = fs.groupby('Sales Rep').sum().reset_index()
#safety to prevent any unwanted NAN
fg = fg.fillna(0)

fx = fg.merge(fs, on='Sales Rep')
fx['Progress Margin'] = fx['Gross Profit']/fx['Extended Price'] * 100 
print(fx.head())
print('here is sales doc')
print(fs.head())
#create new dataframe of cols to go to csv for dataloader upload
outfp = fx[['Record ID', 'Progress Margin', 'Extended Price']]
outfp = outfp.rename(columns={'Extended Price': 'Progress Amount'})
#print(outfp)
#bye 
#outfp.to_csv(csv_foliar, index=False)

#bent
bs = pd.read_csv(dl_bent)
bg = pd.read_csv(bent)
bs = bs.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep'})

bs = bs.groupby('Sales Rep').sum().reset_index()
bg = bg.fillna(0)

bx = bg.merge(bs, on='Sales Rep')
bx['Progress Margin'] = bx['Gross Profit']/bx['Extended Price'] * 100 
outbp = bx[['Record ID', 'Progress Margin', 'Extended Price']]
outbp = outbp.rename(columns={'Extended Price': 'Progress Amount'})
#outbp.to_csv(csv_bent, index=False)

#AT
at = pd.read_csv(dl_at)

at = at.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep'})

at = at.groupby('Sales Rep').sum().reset_index()
ag = ag.fillna(0)

ax = ag.merge(at, on='Sales Rep')
ax['Progress Margin'] = ax['Gross Profit']/ax['Extended Price'] * 100 
outat = ax[['Record ID', 'Progress Margin', 'Extended Price']]
outat = outat.rename(columns={'Extended Price': 'Progress Amount'})
#outat.to_csv(csv_at, index=False)

#armor
ar = pd.read_csv(dl_armor)
arg = pd.read_csv(armor)
ar = ar.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep'})

ar = ar.groupby('Sales Rep').sum().reset_index()
arg = arg.fillna(0)

arx = arg.merge(ar, on='Sales Rep')
arx['Progress Margin'] = arx['Gross Profit']/arx['Extended Price'] * 100 
outar = arx[['Record ID', 'Progress Margin', 'Extended Price']]
outar = outar.rename(columns={'Extended Price': 'Progress Amount'})
#outar.to_csv(csv_armor, index=False)

print('********** test here **********')
print(arx[['Sales Goal Name', 'Extended Price', 'Progress Margin',]])

all = pd.concat([outfp, outbp, outat, outar],ignore_index=True,  sort=False)

all.to_csv(today, index=False)
