import pandas as pd
import numpy as np
import xlsxwriter

file = r"C:\Users\AJ Hephner\Desktop\testsplit.xlsx"


r = pd.read_excel(file)
r.describe()
r.drop_duplicates(keep='first')

opFile = r"C:\Users\AJ Hephner\Desktop\Opp Products.xlsx"
op = pd.read_excel(opFile)
op.describe()

op_u = op.drop_duplicates()
op_u.describe()

ap = r"C:\Users\AJ Hephner\Desktop\ATS Products in SF.xlsx"
sf = pd.read_excel(ap)
sf.describe()
sf.info()

#rename cols to match
op = op_u.rename(columns = {'ATS_Product__c': 'Id'})

#type string
op = op['Id'].astype(str)
sf = sf.astype(str)

#merge file
combine2 = pd.merge(sf, op , on = 'Id', how='right', indicator= True) #-> want 1387 lines that is how many are unique to op
combine2.describe()

#excel
combine2.to_excel(filename)
