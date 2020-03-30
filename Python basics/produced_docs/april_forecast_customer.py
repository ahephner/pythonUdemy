#copy paste from jupyiter file why it would flow well if copy pasted into vs code 
import pandas as pd
df = pd.read_csv(filepath)
df.head()

march = df[df['Doc Month']==3]
april = df[df['Doc Month']==4]

#make a copy of the original df by month then start the process of cleaning will join 
#with april lower then we will join the reps by workbench folder
dfm = march.copy()

dfm = dfm[['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price']]
#combine sales then verify vs report in sf
dfm = dfm.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name']).sum().reset_index()
dfm.tail()
#find accounts where the rep on the doc is different than the owner then 
#make the new owner the doc rep
newOwner = dfm[dfm['Sales Rep (Doc): Sales Rep']!= dfm['Sales Rep: Sales Rep']]
newOwner['Sales Rep (Doc): Sales Rep'] = newOwner['Sales Rep: Sales Rep']

#reverse of the idea above only get accounts where current owner also made sale last year
sameOwner = dfm[dfm['Sales Rep (Doc): Sales Rep'] == dfm['Sales Rep: Sales Rep']]

#make sure row numbers match dfm dataframe
dfm.info()
newOwner.info()
sameOwner.info()

#join march sales together
joinMarch = sameOwner.merge(newOwner, on=['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price'], how='outer')

#select cols i need then rename total to indicate march sales
joinMarch = joinMarch[['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price']]
joinMarch = joinMarch.rename(columns={'Extended Price': 'March 2019'})
#verify totals against report
joinMarch.head()

##
###April same as above
##
dfa = april.copy()
dfa = dfa[['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price']]
dfa = dfa.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name']).sum().reset_index()
dfa.head()

dfa = dfa.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name']).sum().reset_index()

aprilNewOwner['Sales Rep (Doc): Sales Rep'] = aprilNewOwner['Sales Rep: Sales Rep']
aprilSameOwner = dfa[dfa['Sales Rep (Doc): Sales Rep'] == dfa['Sales Rep: Sales Rep']]

dfa.info()
aprilNewOwner.info()
aprilSameOwner.info()
joinedApril = aprilSameOwner.merge(aprilNewOwner, on=['Real Account ID', 'Sales Rep (Doc): Sales Rep','Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price'], how='outer')
joinedApril = joinedApril[['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Extended Price']]
joinedApril = joinedApril.rename(columns={'Extended Price': 'April 2019'})

#
##Join two months
#
#indicator is a way to see if sales were in both months 
all = joinedApril.merge(joinMarch,
                       on=['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 'Customer Name'], how='outer', 
                        indicator=True)
 #fill Na values if account had samles in one month not other
 values = {'April 2019': 0, 'March 2019': 0}
 all =all.fillna(value=values)
 
 #add columns we need to pass to dataloader
 all['Goal name'] = all['Sales Rep: Sales Rep']+'('+all['Customer #']+')'+" April '20"
 all['Budget Type'] = 'Monthly Sales'
 all['Start Date'] = '4/1/2020'
 all['Start Date'] = '4/30/2020'
 all['Budget Amount'] = 0
 all['Forecast Amount'] = 0
 
 #
 ##Rep id join
 #
 #need rep id for sales goal to be created and added to rep page
 rep= pd.read_csv(rFILEPATH)
 rep = rep.rename(columns={'Name': 'Sales Rep: Sales Rep'})
 all = all.merge(rep, on='Sales Rep: Sales Rep', how= 'outer')
 
 #bye
 all.to_csv(rFILEPATH, index=False)
 
 
 
 
 
