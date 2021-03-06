#error on copy- future FYI I brought in from CSV file and had calcs covered. This threw an error as the calc was a string under number
#redid the list by totally scrubbing the file to just numbers and strings then converted to csv utf-8
import matplotlib.pyplot as py
import numpy as np 



#COPIED LISTS
park =['Holl','RSP','RS','HP','RWNP','CCNA','FE','HM','LRE','CUM','HPP','HRE','HW','FJH','DUR','GE','BCC','CYN','HSEJH','HSEHS','FFCP','OF','FCI','FCJH','FCE','TCE','CRE','ADMIN','Bus','NBE','HTP','HPE','BRP','FHS','SCE','SCI','MSF','SAX','BSP','BSE']
hours=[2075,350,1246,881,451.5,506,446,211,426,1857,778,388,400,500,509.3,544.5,394.6,1780,669.75,2596.65,1476.3,1829.7,534.5,878.13,261.3,749.6,161,139.12,190.1,391,878.86,312.4,4243.442,1617,233.6,197.12,822,432,1078,618.33]
wo = [1278,	250,462,635,549,241,371,113,363,969,688,127,524,134,255,199,446,872,330,779,656,965,120,218,97,132,191,48,94,211,924,121,1557,712,70,69,652,366,656,362]
ft_labor=[55790.06,10059.86,36249.22,26558.38,11699.57,13597.08,11886.65,6263.86,8222.67,34112.22,15168.57,6842.12,8554.51,9847.82,13196.02,14513.12,10614.93,50193.65,18152.84,73903.42,40936.5,50291.66,12284.93,25619.56,7060.12,20998.41,2826.79,2627.69,3628.97,6861.83,18696.7,5819.31,107244.1,39519.94,5734.12,4429.08,19025.83,11025.7,28284.83,16179.76]
pt_labor=[4875.6,556.34,2707.42,1461.73,1131.31,898.63,558.89,188.72,1969.94,5313.88,2874.83,1554.04,986,1788.29,2930.75,3089.92,1822.3,7627.47,3534.19,10570.17,6516.96,6058.08,2154.48,2902.17,753.62,3781.57,825.9,506.35,955.22,1442.48,2186.76,1530.88,6524.06,2811.11,570.8,367.5,1235.02,467.6,5300.28,3169.26]
tools=[9426.02,735.83,4898.48,2425.03,479.82,210.32,501.16,631.7,45,18099.13,99.16,42.81,1980.86,185.88,0,26.65,1308.33,17771.89,1706.42,9791.16,13159.45,6024.43,303.6,776.5,270.95,994.11,0,44.89,1394.676,0,1636.91,30,23454.3,2531.41,1547.05,0,4715.09,96.76,3879.35,633.27]
service=[30685.98,4043.92,13891.12,1171.11,0,766.7,1368,205.2,0,38123.49,2426,5895.4,0,4505.4,1368,8765.8,0,9476.68,3329.8,17880.79,4534.53,4076.39,1938,1997.3,1425,5264.8,2394,1368,0,2109,8773.26,1767,29399.8,15378.1,6088.8,3249.5,51311.34,263.2,4837.38,5844.4]
mlc=[139.00,41.75,124.50,78.25,41.25,37.00,45.75,36.00,85.50,604.50,193.00,97.75,103.40,120.25,3.00,4.00,6.90,19.90,2.00,247.00,29.40,114.30,124.00,43.00,19.40,46.00,40.00,31.00,38.00,121.50,225.00,67.75,768.00,345.50,33.50,51.00,204.00,97.50,18.90,17.25]
#create empty list combine pt & ft labor 
clabor = []
clabor.append(ft_labor)
clabor.append(pt_labor)

#use the zip(*) to get the two arrays to add together to get labor cost
full_labor = [sum(x) for x in zip(*clabor)]

#convert wo to numpy
npwo = np.array(wo)

np_wo= npwo * 2 

ind = np.arange(len(park))

#plots below first is efficency of WO per park 
fig = py.figure()
fig.suptitle('WO Completed', fontsize = 14, fontweight = 'bold')
#adding subheader 
#subplot(nrows, ncolumns, plot_number)
ax = fig.add_subplot(111)
fig.subplots_adjust(top = 0.85)


#y axis
py.ylabel('Booked Hours', fontsize=22, fontweight = 'bold')


#x axis
py.xlabel('Cost', fontsize = 22, fontweight = 'bold')

#graph body
 
py.scatter(ft_labor, hours, s=np_wo, label=park)



py.grid(True)
py.show()
py.clf()

#bar Chart
py.xlabel('Part-Time Labor Hours', fontsize = 20, fontweight = 'bold')
py.ylabel('Cost', fontsize=20, fontweight = 'bold')
py.xticks(ind, park, fontsize = 15)
py.yticks(fontsize = 15)
py.bar(ind, pt_labor)


py.show()
py.clf()
