# Using a histogram graph its best to use squareroot of the number 
# of data points to plot the bins. This example shows how to do show
# note matplotlib and seaborn are already imported 
# from datacamp

# Import numpy
import numpy as np

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins

n_bins= int(n_bins)
# Plot the histogram
plt.hist(versicolor_petal_length, bins= n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()