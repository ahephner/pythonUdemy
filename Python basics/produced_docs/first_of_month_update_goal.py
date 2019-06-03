# ONLY RUN FOR MONTH YOU NEED TO DO

# To run updates go to SF and run any sales report with all the reps I prefer Sales Analysis By Rep, 
#run it for previous month i.e. 4/1/2019-4/30/2019 then export to Excel save as 'last month act' 

# Then go to dataloader export goal for that month soql should look like this but update the correct month:

# SELECT Id, Progress_Amount__c, Name, Sales_Rep__c FROM Sales_Goal__c 
# WHERE Budget_Type__c = 'Monthly Sales' AND Inactive__c = false AND Date__c = 2019-05-01

# Run script export and then update in dataloader

import pandas as pd
act = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\Work Bench\prev month actual.csv')
goal = pd.read_csv(r'C:\Users\AJ Hephner\Documents\2019\Work Bench\Prev month goal.csv')
rep = pd.read_csv(r"C:\Users\AJ Hephner\Documents\2019\Work Bench\reps_id.csv")

rep = rep.rename(columns={'Id': 'Sales Rep'})
rep.head(2)

goal = goal.merge( rep, on='Sales Rep',  how='outer')
goal.head(4)

act = act.rename(columns={'Sales Rep': 'Name'})
act.head()

act = pd.merge(act, goal, on='Name', how='outer')
act.head(20)

final = act[['Record ID','Progress Amount_x']]
final = final.rename(columns={'Progress Amount_x': 'Progress Amount'})
final.head()
final = final.dropna()
#bye
final.to_csv(r"C:\Users\AJ Hephner\Documents\2019\Work Bench\update.csv", index=False)


