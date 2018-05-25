#df is preloaded value

# Print the value counts for 'Site Fill'
#pass column inside [].value_counts -> gives a number of values that each row reps
#i.e. if 10 Indiana you would see IN 10
#(dropna = False) -> return values that are NaN
print(df['Site Fill'].value_counts(dropna = False))


#showing data off a .describe()

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
# grabbing column 
# .kind = 'hist' want to use a histogram 
# Be sure to rescale both axes using logx=True and logy=True
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()


# boxplot
# its also using pandas as well 
# Great way to show outlier in data and compair to objects. Like here we are looking
# at the cost of land by Borough

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()

# Boxplots are great when you have a numeric column that you want to compare across different categories.
# When you want to visualize two numeric columns, scatter plots are ideal.

#kind = 'scatter' 
df_subset.plot(kind='scatter', x = 'initial_cost', y='total_est_fee', rot=70)
