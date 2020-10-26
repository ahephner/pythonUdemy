#This allows up to export reports from SF and see what customer purchased prior to the SGM. Then we can upload to the account obj. 
#Useful because you can't show accounts purchase history if they have never bought anything prior to sgm purchase
#Verify report https://advancedturf.lightning.force.com/lightning/r/Report/00O2M0000099JI5UAM/view

import pandas as pd
from datetime import datetime
#accounts
acc = pd.read_csv(r'filepath')
#sales raw
df = pd.read_csv(r'filepath', encoding= 'unicode_escape')

#make sure datetimes are clean
df['Doc Date'] = df['Doc Date'].apply(pd.to_datetime, errors='ignore')
df['Steel Green Purchase Date'] = df['Steel Green Purchase Date'].apply(pd.to_datetime, errors='ignore')

#get boolean to filter on
df['before'] = df['Doc Date'] < df['Steel Green Purchase Date']
before = df[df['before'] == True]

#sum
before = before.groupby(['Account Name', 'Real Account ID']).sum().reset_index()
before.head(10)
before = before.fillna(0)
#bye
before.to_csv(r'filepath')
