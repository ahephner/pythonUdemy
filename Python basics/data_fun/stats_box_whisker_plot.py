import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

file = r'C:\Users\ajhep\Desktop\dataexamples.xlsx'
df = pd.read_excel(file) 

print(df.head())

# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y = 'petal length (cm)', data= df)
_ = sns.swarmplot(x='species', y = 'petal length (cm)', size=10, data= df)
# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
plt.clf()

#How box plot works 
data_set= [2,43,49,50,51,51,53,54,60,62,63]

example = sns.boxplot(data= data_set)
plt.xlabel('numbers')
plt.show()

# median = 51 
# lower whisker = 43 2 is an outlier
# lower quartile = 49
# median = 51 (odd set so take number of points +1 /2 for position of median)
# upper quartile = 60
# upper whisker = 63

# Cal. outlier:

# take (upper quartile - lower quartile) * 1.5 = 16.5
# anything greater than 60 + 16.5 or less than 49 - 16.5 are outliers in this case 2  
