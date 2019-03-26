import numpy as np 
import pandas as pd 
from datetime import datetime, timedelta

#all sales lines files
ly_arm = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\dataloader Armortech.csv"
ly_fp = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\dataloader Foliar.csv"
ly_at = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\dataloader AT.csv"
ly_bent = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\dataloader Bentgrass.csv"

#goals to look at 
arm = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\Goal Armortech.csv"
fp = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\Goal Foliar.csv"
at = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\goalsAT.csv"
bent = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\Goal Bentgrass.csv"

#landing page
land = r"C:\Users\AJ Hephner\Documents\2019\Goals Upload\Last Year\landing.csv"

#set up time var. 

x = datetime.now() - timedelta(days=365)
print(x)


#aromortech here is the general guide to what the pattern the rest of the code is doing.
larm = pd.read_csv(ly_arm)
latgoal = pd.read_csv(arm)
#clean dataframe
larm = larm.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep', 'Extended Price': 'Prev YTD Sales'})
larm['Doc Date'] = pd.to_datetime(larm['Doc Date'])
larm = larm[larm['Doc Date']<= x]

#math
larm = larm.groupby('Sales Rep').sum().reset_index()
larm = larm.fillna(0)
larm['Prev YTD Margin'] = larm['Gross Profit'] / larm['Prev YTD Sales'] * 100 

#merge and select values
arm_merge = latgoal.merge(larm, on='Sales Rep')
print('********** armor here **********')
print(arm_merge[['Sales Goal Name', 'Prev YTD Margin', 'Prev YTD Sales']])
#will combine this df with others to send to csv...only one upload vs 4
arm_out = arm_merge[['Record ID', 'Prev YTD Margin', 'Prev YTD Sales']]
#print(at_out)

#foliar pak
lfp= pd.read_csv(ly_fp)
fpgoal = pd.read_csv(fp)
lfp = lfp.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep', 'Extended Price': 'Prev YTD Sales'})
lfp['Doc Date'] = pd.to_datetime(lfp['Doc Date'])
lfp = lfp[lfp['Doc Date']<= x]

lfp = lfp.groupby('Sales Rep').sum().reset_index()
lfp = lfp.fillna(0)
lfp['Prev YTD Margin'] = lfp['Gross Profit'] / lfp['Prev YTD Sales'] * 100 

fp_merge = fpgoal.merge(lfp, on='Sales Rep')
print('********** foliar here **********')
print(fp_merge[['Sales Goal Name', 'Prev YTD Margin', 'Prev YTD Sales']])
fp_out = fp_merge[['Record ID', 'Prev YTD Margin', 'Prev YTD Sales']]

 #AT
lat= pd.read_csv(ly_at)
atgoal = pd.read_csv(at)
lat = lat.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep', 'Extended Price': 'Prev YTD Sales'})
lat['Doc Date'] = pd.to_datetime(lat['Doc Date'])
lat = lat[lat['Doc Date']<= x]

lat = lat.groupby('Sales Rep').sum().reset_index()
lat = lat.fillna(0)
lat['Prev YTD Margin'] = lat['Gross Profit'] / lat['Prev YTD Sales'] * 100 

at_merge = atgoal.merge(lat, on='Sales Rep')
print('********** AT here **********')
print(at_merge[['Sales Goal Name', 'Prev YTD Margin', 'Prev YTD Sales']])
at_out = at_merge[['Record ID', 'Prev YTD Margin', 'Prev YTD Sales']]

#bent
lb= pd.read_csv(ly_bent)
bgoal = pd.read_csv(bent)
lb = lb.rename(columns={'Sales_Document__r.Sales Rep (Doc)':'Sales Rep', 'Extended Price': 'Prev YTD Sales'})
lb['Doc Date'] = pd.to_datetime(lb['Doc Date'])
lb = lb[lb['Doc Date']<= x]

lb = lb.groupby('Sales Rep').sum().reset_index()
lb = lb.fillna(0)
lb['Prev YTD Margin'] = lb['Gross Profit'] / lb['Prev YTD Sales'] * 100 

bent_merge = bgoal.merge(lb, on='Sales Rep')
print('********** bent here **********')
print(bent_merge[['Sales Goal Name', 'Prev YTD Margin', 'Prev YTD Sales']])
bent_out = bent_merge[['Record ID', 'Prev YTD Margin', 'Prev YTD Sales']]

#concat all dfs 
all = pd.concat([arm_out, fp_out, at_out, bent_out],ignore_index=True,  sort=False)
print('********** concat here **********')
#print(all)

#bye
all.to_csv(land, index=False)
