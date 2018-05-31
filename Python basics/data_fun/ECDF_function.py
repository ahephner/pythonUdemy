import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    #sort the data out 
    x = np.sort(data)

    # y-data for the ECDF: y
    #np.arange(start, stop)/step  
    y = np.arange(1, n+1) / n

    return x, y

    #using function to graph below showing age distribution

file = r"C:\Users\ajhep\Desktop\python.xlsx"

df = pd.read_excel(file, index_col = 0)

#converting to np.array for example 
num = np.array(df['AGE'])
# print(type(num))


    # Compute ECDF for versicolor data: x_vers, y_vers
    #data would go into the function
x_vers, y_vers = ecdf(num)

# Generate plot
#returns a distribution plot so we want no line and each point is a dot
plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
plt.xlabel('something')
plt.ylabel('hey')

plt.show()


