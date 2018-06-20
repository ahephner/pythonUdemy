import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

file = pd.read_excel(r"C:\Users\ajhep\Desktop\Focus Products Golf 2018.xlsx")


melt = pd.melt(file, id_vars='Rep', value_vars='Foliar-Pak +PB1')

print(melt.head())