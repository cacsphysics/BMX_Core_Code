import numpy as np
import BMX
import matplotlib.pylab as plt

filename = '20190423-0001 (17).txt'
data1, data2, time, data3, data4 = BMX.BMX_Magnetic_BDOT(filename, data_Structure = 'ztzt')
#name = 'ztzt'
#data = BMX.BMX_Pico_Read(filename)
#my_Dict = {'%s'%filename: filename}
#print(my_Dict['%s'%filename])
#BMX.bDot_Array_Name('z')

