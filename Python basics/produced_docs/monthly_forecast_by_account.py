import pandas as pd

dfa = pd.read_csv(rfilepath)
dfs = pd.read_csv(rfilepath)
dfa = pd.read_csv(rfilepath)
rep = pd.read_csv(rfilepath)

print(dfs.info())

#Seperate sales into two dataframes one with new account owners one with same run .info to make sure counts equal original 
same = dfs[dfs['Sales Rep (Doc): Sales Rep'] == dfs['Sales Rep: Sales Rep']]
print('same')
print(same.info())

newOwner = dfs[dfs['Sales Rep (Doc): Sales Rep'] != dfs['Sales Rep: Sales Rep']]
print('newOwnerInfo')
print(newOwner.info())

#groupby and some both df's
same = same[['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price']]
same = same.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name']).sum().reset_index()

newOwner = newOwner[['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price']]
newOwner = newOwner.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name']).sum().reset_index()

#here is a good place to call .head() and verify vs. Salesforce Report #
print('same total')
print(same.head(3))
print('newOwner total')
print(newOwner.head(3))

#make new owner doc same as owner les people see sales totals from last year
#even if they are not owner then 
newOwner['Sales Rep (Doc): Sales Rep'] = newOwner['Sales Rep: Sales Rep']

#join them together
js = same.merge(newOwner, on=['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price'], how='outer')
print('joined')
print(js.info())

#join all accounts w/out sales
all = dfa.merge(js, on=['Real Account ID', 'Customer Name', 'Customer #', 'Sales Rep: Sales Rep'], how='outer', indicator=True)

#use the merge field to filter out values
#if right they are no longer an active account
#left only means they don't have sales history in timeframe of goals
left = all[all["_merge"]=='left_only']

#use values to fill in na
values = {'Sales Rep(Doc): Sales Rep': 'NA','Extended Price': 0}
left = left.fillna(value=values)
print('left Head')
print(left.head())

#merge them
final = both.merge(left, on=['Real Account ID', 'Customer Name', 'Customer #','Sales Rep: Sales Rep', 'Extended Price'], how='outer')
f = f.rename(columns={'Sales Rep: Sales Rep': 'Rep', 'Extended Price': 'May 19'})

#certain high volume reps don't use all accounts select the accounts with sales 1k and better
#then remove them from the master list
bucci = f[(f['Rep'].str.contains('Bucci')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Bucci')]
smith = f[(f['Rep'].str.contains('Roy Smith')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Roy Smith')]
bash = f[(f['Rep'].str.contains('Bash')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Bash')]
petrosky = f[(f['Rep'].str.contains('Petrosky')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Petrosky')]
biddle = f[(f['Rep'].str.contains('Biddle')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Biddle')]
sand = f[(f['Rep'].str.contains('Scott Sand')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Scott Sand')]
tSmith = f[(f['Rep'].str.contains('Todd Smith')) & (f['May 19']>999)]
f = f[~f['Rep'].str.contains('Todd Smith')]

#append the above then add back to master list
largeReps = bucci.append([ smith, bash, petrosky, biddle, sand, tSmith])
f = f.append(largeReps)

#add in rep info
rep = rep.rename(columns={"Name": "Rep"})
f = f.merge(rep, on='Rep', how= 'outer')

#format the rest of the columns value

f['Goal name'] = f['Rep']+'('+f['Customer #']+')'+" April '20"
f['Budget Type'] = 'Monthly Sales'
f['Start Date'] = '5/1/2020'
f['End Date'] = '5/31/2020'
f['Forecast Amount'] = 0

print('here are all columns')
print(f.head(10))

#add previousmonth sale
prevMonth = prevMonth[["Real Account ID", 'Customer #', 'Extended Price']]
prevMonth = prevMonth.rename(columns={"Extended Price": "April 2020"})
prevMonth = prevMonth.groupby(['Real Account ID','Customer #']).sum().reset_index()

f = f.merge(prevMonth, on=['Real Account ID', 'Customer #'], how='outer', indicator=True)
 #kick right only out should be from reps accounts we excluded above
 f = f[~f['_merge'].str.contains('right_only')]
 secondValue = {'April 2020': 0, 'Customer Name': 'None'}
f = f.fillna(value=secondValue)

#get rid of walk in accounts
f= f[~f['Customer Name'].str.contains('WALK-IN')]
#drop NA
f = f.dropna()

#bye
f.to_csv(filepath, index=False)











