#must have pandas .25. This is how we solved for making sure every account had at least an entry of the desired forecast focus group. 
#you pass the column into the df as a list. Then the .explode unpacks the list and makes it so every item in teh list gets a new row with the 
#df. 

import pandas as pd

df = pd.read_csv(r'file')

l = ['one', 'two', 4, 'five']

df['newCol'] = df.apply(lambda x: cat, axis=1 )

df = df.explode('newCol')
