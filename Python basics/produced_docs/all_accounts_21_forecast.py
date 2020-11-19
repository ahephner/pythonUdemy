#Notes
#Need to make sure the account report does not try to say less than 2000 it will mess up the sports turf account out put
#sales rep -> vs actual rep looks like an issue look into that append vs. merge
#Prev Sales Goal Export can we get the customer name w/o the # also get the customer # in seperate col?
#All data comes from csv exports in salesforce. Check Folder Python Reports in Dev Folder
#Copy/paste from a Jupyter file. So trying to run in straight ide may not work Jupyter is free go download

import pandas as pd 
#files
rep = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2021\Goals\reps_id.csv")
prev_sales = pd.read_csv(r)
prev_goal = pd.read_csv(r)
accounts = pd.read_csv(r)
cur_sales = pd.read_csv(r)

#remove 20000 accounts 
prev_sales['Customer #'] = prev_sales['Customer #'].astype(str)
accounts['Customer #'] = accounts['Customer #'].astype(str)
cur_sales['Customer #'] = cur_sales['Customer #'].astype(str)

cur_sales = cur_sales[~cur_sales['Customer #'].str.startswith('2')]
accounts = accounts[~accounts['Customer #'].str.startswith('2')]
prev_sales = prev_sales[~prev_sales['Customer #'].str.startswith('2')]

#handle transfers
sameRepSLY = prev_sales[prev_sales['Sales Rep (Doc): Sales Rep'] == prev_sales['Sales Rep: Sales Rep']]
newRepSLY = prev_sales[prev_sales['Sales Rep (Doc): Sales Rep'] != prev_sales['Sales Rep: Sales Rep']]

sameRepSLY = sameRepSLY.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()
newRepSLY = newRepSLY.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()
newRepSLY['Sales Rep (Doc): Sales Rep'] = newRepSLY['Sales Rep: Sales Rep']
prevSales = sameRepSLY.append(newRepSLY)
#need to sum again to combine transfer
prevSales = prevSales.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()

#current year sales and transfers
sameRepCY = cur_sales[cur_sales['Sales Rep (Doc): Sales Rep'] == cur_sales['Sales Rep: Sales Rep']]
newRepCY = cur_sales[cur_sales['Sales Rep (Doc): Sales Rep'] != cur_sales['Sales Rep: Sales Rep']]

sameRepCY = sameRepCY.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()
newRepCY = newRepCY.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()
newRepCY['Sales Rep (Doc): Sales Rep'] = newRepCY['Sales Rep: Sales Rep']
curSales = sameRepCY.append(newRepCY)
curSales = curSales.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()

#set margin prep to merge accounts df
curSales['Margin'] = ((curSales['Gross Profit']/curSales['Extended Price']) * 100)
prevSales['Margin'] = ((prevSales['Gross Profit']/prevSales['Extended Price']) * 100)
prevSales = prevSales.rename(columns={'Extended Price': 'Prev Sales', 'Margin': 'Prev Margin'})

curSales = curSales[['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 
                     'Customer Name', 'Cur Sales', 'Cur Margin']]
prevSales = prevSales[['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 
                     'Customer Name', 'Cur Sales', 'Cur Margin']]  
                     
#merge accounts
sa = accounts.merge(curSales, on=['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 
                     'Customer Name'], how='outer', indicator=True)
             
#right only will show accounts that didn't make it in my testing it normally means account set up between the time I run file and the time the code compiled 
#--> Can't merge indicator True 2? so I reset the df inbetween     

right = sa[sa['_merge'] == 'right_only']
print('right only '+right)

sa = sa[['Sales Rep: Sales Rep', 'Customer Name', 'Real Account ID', 'Customer #',
         'Cur Sales', 'Cur Margin']]
sa = sa.merge(prevSales, on=['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 
                     'Customer Name'], how='outer',indicator = True) 
                     
sa = sa[['Sales Rep: Sales Rep', 'Customer Name', 'Real Account ID', 'Customer #',
         'Cur Sales', 'Cur Margin', 'Prev Sales', 'Prev Margin']]

#Now we will join with the previous forecast amount 
#--> reframe the dataframe to grab cols you need 
#--> clean NaN values         
prev_goal = prev_goal.rename(columns={'Sales Goal: Real Account ID': 'Real Account ID', 'Forecast Amount': 'Prev Forecast'})
withGoal = sa.merge(prev_goal,on=['Real Account ID', 'Sales Rep: Sales Rep'], how='outer', indicator=True)

withGoal = withGoal[['Sales Rep: Sales Rep', 'Customer Name', 'Real Account ID', 'Customer #',
                      'Cur Sales', 'Cur Margin', 'Prev Sales', 'Prev Margin', 'Prev Forecast']]
#---> Lets join reps and add detail columns then export
rep = rep.rename(columns={'Name': 'Sales Rep: Sales Rep'})
withReps = withGoal.merge(rep, on ='Sales Rep: Sales Rep',how='outer' )

values = {'Cur Sales': 0, 'Cur Margin':0, 'Prev Sales': 0, 'Prev Margin':0, 'Prev Forecast': 0}
out = withReps
out = out.fillna(value=values)
out['Goal Name']= "2020/21 "+out['Sales Rep: Sales Rep'] +'('+out['Customer #']+')'
out['Budget Type'] = 'Annual Account Forecast'
out['Start Date'] = '10/1/2020'
out['End Date'] = '09/30/2021'
out['Forecast Amount'] = 0

#test
test = out[out['Sales Rep: Sales Rep'].str.contains('Winter')]

#bye
out.to_csv(rfilepaht)
