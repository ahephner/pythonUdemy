# Different type of graph than histogram for snap shot of large data set 
# need to make sure that the data is arranged so each row is a new observation
# and each column is a feature example below: 
# team    city   nickname
# CHI     CHICAGO    Bears
# GB      GREEN BAY  Packers
# DET     DETRIOT    Lions 

# Create bee swarm plot with Seaborn's default settings
import matplotlib.pyplot as plt
import seaborn as sns 
_ = sns.swarmplot(x='species', y = 'petal length (cm)', data = df)

# Label the axes
_ = plt.xlabel('species')
_= plt.ylabel('petal length')

# Show the plot

plt.show()