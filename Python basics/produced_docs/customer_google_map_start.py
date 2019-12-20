import pandas as pd

df = pd.read_csv(rfile)

df.head()

df = df.groupby(['Customer #','Account Name', 'Billing Street', 'Billing City', 'Billing State/Province', 'Billing Zip/Postal Code']).sum().reset_index()
#dont times by 100 if uploading in excel use excel format cell as percent instead
df['Margin'] = df['Gross Profit']/df['Extended Price'] * 100
df.to_csv(r"C:\Users\AJ Hephner\Desktop\python landings\beever.csv",index=False)
