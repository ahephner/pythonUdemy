import pandas as pd

#static reps salesforce id...had to use workbench to get
rep_id = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\Sales Reps Salesforce ID.csv")
doc = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\Sales Detail 5_15.csv")
goals = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\Customer Goals.csv")   

# If you need to append a downloaded excel file do it here. I.E. if you ran all sales last month 
# and then run it just from that date through today please add the downloaded file here    
#download= pd.read_csv(rDOWNLOADED FILE HERE)

goals = goals.fillna(0)

#If you are adding onto the doc file instead of running the entire year uncomment here
#doc = doc.append(download)

doc = doc.drop_duplicates(subset='Sales doc Detail ID', keep='first')
doc = doc.merge(rep_id, on='Sales Rep (Doc): Sales Rep')
#Real Account ID is a formula field on the doc
df = doc[['Extended Price', 'Real Account ID', 'Id']]

df = df.groupby(['Real Account ID', 'Id']).sum().reset_index()

df = df.rename(columns={'Real Account ID': 'Customer', 'Id': 'Sales Rep'})

merged = df.merge(goals, on=['Customer', 'Sales Rep'])
#this is to set up for future uploads so we don't have to upsert as many records
merged['Total Sales'] = merged['Extended Price'] 

out = merged[['Record ID', 'Extended Price']]
#bye
out.to_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\landing.csv", index=False)

#i like to save a copy of what the last upload was for review
snapshot = merged
snapshot.to_csv(r"C:\Users\AJ Hephner\Documents\2019\All Customer Goals\lastRun_snapshot.csv", index=False)
