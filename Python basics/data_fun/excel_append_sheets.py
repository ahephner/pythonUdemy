import pandas as pd

#single worksheet
# Import the data
nyse = pd.read_excel('listings.xlsx', sheetname = 'nyse', 
na_values='n/a')

# Display the head of the data
print(nyse.head())

# Inspect the data
nyse.info()
 

 #extract sheet names from a workbook

 # Create pd.ExcelFile() object
xls = pd.ExcelFile('listings.xlsx')

# Extract sheet names and store in exchanges
exchanges = xls.sheet_names

#extract single sheet name
#nyse = pd.read_excel(xls, sheetname='nyse', na_values='n/a')

# Create listings dictionary with all sheet data
listings = pd.read_excel(xls, sheetname=exchanges, na_values='n/a')
print(listings)
# Inspect NASDAQ listings
listings['nasdaq'].info()

#concat to sheets
# Import the NYSE and NASDAQ listings
nyse = pd.read_excel('listings.xlsx', sheetname='nyse', na_values='n/a')
nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a')

# Inspect nyse and nasdaq
nyse.info()
nasdaq.info()

# Add Exchange reference columns
nyse['Exchange'] = 'NYSE'
nasdaq['Exchange'] = 'NASDAQ'

# Concatenate DataFrames  
combined_listings = pd.concat([nyse, nasdaq])

#automate the loading and combining of data from multiple worksheets

# Create the pd.ExcelFile() object
xls = pd.ExcelFile('listings.xlsx')

# Extract the sheet names from xls
exchanges = xls.sheet_names

# Create an empty list: listings
listings = []

# Import the data
for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname=exchange, na_values='n/a')
    listing['Exchange'] = exchange
    listings.append(listing)

# Concatenate the listings: listing_data
listing_data = pd.concat(listings)

# Inspect the results
listing_data.info()
