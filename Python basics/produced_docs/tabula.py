#basic example of converting to csv. 
#great for cpq quote that needs to be converted
#dont have csv open while running

import pandas as pd
import tabula
csv = tabula.convert_into(r'C:\Users\AJ Hephner\Downloads\midwestlandscapeindustriesinc_quote_176801_1579628915.pdf', r"C:\Users\AJ Hephner\Desktop\python landings\B Norris customer.csv", output_format="csv", pages="all")
