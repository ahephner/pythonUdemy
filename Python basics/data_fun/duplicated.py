import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

path = (r"C:\Users\AJ Hephner\Desktop\notinSF.xlsx")

xlsx = pd.ExcelFile(path)

df = pd.read_excel(xlsx)

df['is_duplicated'] = df.duplicated(['Sales Document Name'])

print(df['is_duplicated'].sum())
