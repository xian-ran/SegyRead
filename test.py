from SegyRead import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
fileName = '../HorizonTracking/f3_xline300_700inline100_400time4_1848.sgy'
data = np.zeros([462,200])
for i in range(200):
    data[:,i] = ReadOneTrace(fileName,i,462)

Wiggle(data,0.1)
