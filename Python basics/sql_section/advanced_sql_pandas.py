# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('Select * from Employee Where EmployeeID >= 6 Order By BirthDate', engine)

# Print head of DataFrame
print(df.head())
