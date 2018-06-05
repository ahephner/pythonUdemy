import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

#This is a useful shorthand for boolean indexing based on index values above or below certain thresholds.
file = pd.read_excel(r"C:\Users\ajhep\Desktop\dataexamples.xlsx")


file.truncate(before =1, after=4)

#can do on dates as well basically limit the data to come back in pandas

