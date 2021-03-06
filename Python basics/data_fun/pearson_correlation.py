import numpy as np 
import pandas as pd 
# this is a way to find the correlation of two variables along a scattered plot
# measure the strenght of relationship for two variables 
# if you get positive number that means the trend is positive 
# if you get a negative number the trend is down 
# if you get a flat number that means there is no trend
# range can only be from -1 to 1 
# 1 = complete correlation
# -1 = anti-correlation
# 0 no correlation 
length = np.array([4.1,4.5,4.9,4,4.6,4.5,4.7,3.3,4.6,3.9,3.5,4.2,4,4.7,3.6,4.4,4.5,4.1,4.5])
width = np.array([1.4,1.5,1.5,1.3,1.5,1.3,1.6,1,1.2,1.4,1.5,1,1.4,1.3,1.3,1.5,1,1.5,1.8])


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1] because above returns an answer 2d array this will return just one line 
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor
r = pearson_r(length, width)

# Print the result
print(r)