import pandas as pd

rep = pd.read_csv(r'C:\Users\ajhep\OneDrive\Documents\python sheets\reps_id.csv')
prev_sales = pd.read_csv(r"D:\lySales.csv")
prev_goal = pd.read_csv(r"D:\lySalesGoals.csv")
accounts = pd.read_csv(r"D:\accounts.csv")
cur_sales = pd.read_csv(r"D:\cySales.csv")

#remove 200's accounts
prev_sales['Customer #'] = prev_sales['Customer #'].astype(str)
accounts['Customer #'] = accounts['Customer #'].astype(str)
cur_sales['Customer #'] = cur_sales['Customer #'].astype(str)
cur_sales = cur_sales[~cur_sales['Customer #'].str.startswith('2')]
accounts = accounts[~accounts['Customer #'].str.startswith('2')]
prev_sales = prev_sales[~prev_sales['Customer #'].str.startswith('2')]

#handle transfer accounts
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

prevSales['Margin'] = ((prevSales['Gross Profit']/prevSales['Extended Price']) * 100)

#wittle down columns
prevSales = prevSales[['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 
                     'Customer Name', 'Prev Sales', 'Prev Margin']]  
#merge with all accounts
allacc = accounts.merge(prevSales, on=['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 
                     'Customer Name'], how='outer', indicator=True)
                    
x = allacc[allacc['_merge']=='right_only']
x.info()

left = allacc[allacc['_merge']=='left_only']
values = {'Prev Sales': 0, 'Prev Margin': 0}
left = left.fillna(value=values)

allacc = allacc[~allacc['_merge'].str.contains('right')]
allacc = allacc[~allacc['_merge'].str.contains('left')]
both = allacc.append(left)

both = both[['Sales Rep: Sales Rep', 'Customer Name', 'Real Account ID', 'Customer #', 'Prev Sales',
            'Prev Margin']]
#current year sales and transfers 
sameRepCY = cur_sales[cur_sales['Sales Rep (Doc): Sales Rep'] == cur_sales['Sales Rep: Sales Rep']]
newRepCY = cur_sales[cur_sales['Sales Rep (Doc): Sales Rep'] != cur_sales['Sales Rep: Sales Rep']]

sameRepCY = sameRepCY.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()
                                
newRepCY = newRepCY.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()

newRepCY['Sales Rep (Doc): Sales Rep'] = newRepCY['Sales Rep: Sales Rep']
curSales = sameRepCY.append(newRepCY)

#need to sum again 
curSales = curSales.groupby(['Real Account ID', 'Sales Rep (Doc): Sales Rep', 'Sales Rep: Sales Rep', 'Customer #',
                                'Customer Name']).sum().reset_index()
                                
#set margin and prep to merge accounts dataframe
curSales['Margin'] = ((curSales['Gross Profit']/curSales['Extended Price']) * 100)

#rename headers and clean up for join
curSales = curSales.rename(columns={'Extended Price': 'Progress Amount', 'Margin': 'Progress Margin'})

curSales = curSales[['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 'Customer Name', 'Progress Amount',
                    'Progress Margin']]

allgoals = both.merge(curSales, on=['Real Account ID', 'Sales Rep: Sales Rep', 'Customer #', 'Customer Name'],
                     how='outer', indicator=True)
new = allgoals[allgoals['_merge'] == 'right_only']
#make sure you don't pull S accounts in current year
new.info()

allgoals = allgoals.fillna(value = filler)

allgoals = allgoals[['Sales Rep: Sales Rep', 'Customer Name', 'Real Account ID', 'Customer #', 'Prev Sales',
            'Prev Margin', 'Progress Amount', 'Progress Margin']]
            
            
prev_goal = prev_goal.rename(columns={'Sales Goal: Real Account ID':'Real Account ID', 'Forecast Amount':'Prev Forecast'})
withPrev = allgoals.merge(prev_goal,on=['Real Account ID', 'Sales Rep: Sales Rep'], how='outer', indicator=True)

#if merge != both
#right only means transfered account or no longer active
#left onlhy means no forecast for last year

withPrev = withPrev[withPrev['_merge']!='right']

#add reps
rep = rep.rename(columns={'Sales Rep': 'Sales Rep: Sales Rep'})
withReps = withPrev.merge(rep, on ='Sales Rep: Sales Rep',how='outer' )
noRep = withReps[withReps['Id'].isnull()]

withReps = withReps[~withReps['Id'].isnull()]

out = withReps
out = out[['Sales Rep: Sales Rep', 'Id', 'Customer Name', 'Customer #', 'Prev Sales',
       'Prev Margin', 'Progress Amount', 'Progress Margin', 'Prev Forecast', 'Real Account ID']]
na_values = {'Cur Sales': 0, 'Cur Margin':0, 'Prev Sales': 0, 'Prev Margin':0, 'Prev Forecast': 0}
out = out.fillna(value=na_values)

out['Goal Name']= "2021/22 "+out['Sales Rep: Sales Rep'] +'('+out['Customer #']+')'
out['Budget Type'] = 'Annual Account Forecast'
out['Start Date'] = '10/1/2021'
out['End Date'] = '09/30/2022'
out['Forecast Amount'] = 0

#check out na values
is_NaN = out.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = out[row_has_NaN]

print(rows_with_NaN)
out = out.dropna()
out.to_csv(r"C:\Users\ajhep\OneDrive\Documents\python sheets\ATS\salesGoalsSales.csv", index=False)





