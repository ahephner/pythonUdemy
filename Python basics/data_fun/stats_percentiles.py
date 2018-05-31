import numpy as np
import matplotlib.pyplot as plt

versicolor_petal_length = np.array([3.2,3.5, 4.1, 2.9, 2.3, 4.6, 2.2, 3.4, 3.6, 3.76, 4.5, 2.8, 2.1, 3.1, 3.4, 4.6, 3.4])
# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
#returns the values at 2.5%, 25%, 50%, 75% and 97.5% of array
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

# Overlay percentiles as red diamonds.
            #xaxis         yaxis     
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color ='red',
         linestyle ='none')

# Show the plot
plt.show()