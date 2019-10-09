#copy of my Jupyter code
import pandas as pd

#last year sales with gross profit on each line
df = pd.read_csv(r)#run fall goal setting report

#Get Sales by who made the sale to the account 
ly = df.groupby(['Real Account ID', 'Customer #', 'Sales Rep (Doc): Sales Rep']).sum().reset_index()

Get sales totals by who owns the account 
owner = df.groupby(['Real Account ID', 'Customer #', 'Sales Rep: Sales Rep']).sum().reset_index()

#create margin 
ly['Previous Margin'] = (ly['Extended Price']-ly['Extended Cost'])/ly['Extended Price'] * 100 
owner['Previous Margin'] = (owner['Extended Price']-owner['Extended Cost'])/owner['Extended Price'] * 100 

#join the two save this will give me a record for 
#every current owner regardeless if they made a sale last year. We will get previous years sales below
ly = ly.rename(columns={'Sales Rep (Doc): Sales Rep': 'Sales Rep: Sales Rep'})
transfers = ly.merge(owner, on='Real Account ID', how='right')

#save a copy for sales to accounts not owned by doc rep
double = ly.merge(owner,on='Real Account ID', how='right')

transfers.head()
#Account owners are sales rep_y and doc sales rep are _x so if _y = _x then it is a sale to my account
notTransfer = transfers[transfers['Sales Rep: Sales Rep_y'] == transfers['Sales Rep: Sales Rep_x']]
notTransfer.head()
notTransfer = notTransfer[['Real Account ID', 'Customer #_x','Sales Rep: Sales Rep_x', 'Extended Price_x', 'Previous Margin_x' ]]

#hold ready to go
notTransfer = notTransfer.rename(columns={'Customer #_x': 'Customer #', 'Sales Rep: Sales Rep_x': 'Sales Rep', 
                                          'Extended Price_x': 'Extended Price', 'Previous Margin_x': 'Previous Margin'})
                                          
#Exceptions
#Here we are going to see reps who sold to accounts that are not theres and 
#below join it back with the goals. For the most part I try and see if there 
#are a lot of sales to new reps accounts then I will grab the price and margin_y 
#and use that for a goal and change the name of the goal to total sales so they know it's everyone                                          
ds = transfers[(transfers['Sales Rep: Sales Rep_y'] != transfers['Sales Rep: Sales Rep_x']) ]

goals = notTransfer.copy()
goals['Start Date'] = '10/1/2019'
goals['End Date'] = '9/30/2020'
goals['Forecast Amount'] = 0
goals['Budget Amount'] = 0
goals['Budget Amount'] = 0
goals['Budget Type'] = 'Total Sales'
goals['Goal Name'] = '2019/20 '+ goals['Sales Rep']+'('+goals['Customer #']+')'
goals['Inactive'] = 'FALSE'
goals['Current Year'] = 'TRUE'

#join reps
rep= pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\Work Bench\reps_id.csv")
rep = rep.rename(columns={'Name': 'Sales Rep'})
goals = goals.merge(rep, on='Sales Rep', how= 'outer')
goals = goals.rename(columns={'Id': 'Sales Rep Id'})
goals = goals.rename(columns={'Id': 'Sales Rep Id'})
