import numpy as np 
import pandas as pd 
# this is a way to find the correlation of two variables along a scattered plot
#measure the strenght of relationship for two variables 
# if you get positive number that means the trend is positive 
# if you get a negative number the trend is down 
# if you get a flat number that means there is no trend
# range can only be from -1 to 1 
# 1 = complete correlation
# -1 = anti-correlation
# 0 no correlation 
file = r'C:\Users\ajhep\Desktop\dataexamples.xlsx'

read = pd.read_excel(file, sheet_name = 'correlation')


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1] because above returns an answer 2d array this will return just one line 
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor
r = pearson_r(variable_1, variable_2)

# Print the result
print(r)