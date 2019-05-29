import pandas as pd

file = r"C:\Users\AJ Hephner\Downloads\report1559073215660.csv"

df = pd.read_csv(file)
df.describe()

keep1 = df.drop_duplicates(subset='Sales Doc #', keep='first' )
keep1.describe()

#this needs cleaned up not dry at all!!!!!!
#error when doing a groupby that wouldn't let me send out 
#look at .apply()method or a method that will break on rep name
so = keep1[keep1['Sales Rep (Doc): Sales Rep'].str.contains('Grady')]
rs = keep1[keep1['Sales Rep (Doc): Sales Rep'].str.contains('Stachlewitz')]
mp = keep1[keep1['Sales Rep (Doc): Sales Rep'].str.contains('Parent')]
mb = keep1[keep1['Sales Rep (Doc): Sales Rep'].str.contains('Biddle')]
#so on and so forth till all the reps are found 

out = pd.concat([so, rs, mp, mb, jm, jb, hou, eb, eo, db, dj, bw, bh, bf, ba])
out.to_excel(r'C:\Users\AJ Hephner\Documents\JDT\JDT Sales Doc Headers.xlsx', index=False)
