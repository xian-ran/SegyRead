#! /usr/bin/python
#encoding=utf-8

import struct, sys
import numpy as np
import matplotlib.pyplot as plt

def ibm2ieee2(ibm_float):
    """
    ibm2ieee2(ibm_float)
    Used by permission
    (C) Secchi Angelo
    with thanks to Howard Lightstone and Anton Vredegoor. 
    """
    dividend=float(16**6)
    
    if ibm_float == 0:
        return 0.0
    istic,a,b,c=struct.unpack('>BBBB',ibm_float)
    if istic >= 128:
        sign= -1.0
        istic = istic - 128
    else:
        sign = 1.0
    mant= float(a<<16) + float(b<<8) +float(c)
    return sign* 16**(istic-64)*(mant/dividend)

def ReadOneTrace(fileName, trace, sampleNum):
    fp = open(fileName,'rb')
    fp.seek(3600,0)
    for i in range(trace):
        fp.seek(240,1)
        fp.seek(sampleNum*4,1)
    fp.seek(240,1)
    data = fp.read(sampleNum*4)
    value = [];
    for i in range(sampleNum):
        index = i*4
        indexEnd = (i+1)*4
        value.append(ibm2ieee2(data[index:indexEnd]))
    fp.close()
    return value

def Wiggle(data, lWidth):
    sampleNum, traceNum = np.shape(data)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(traceNum):
        traceData = data[:,i]
        maxVal = np.amax(traceData)
        ax.plot(i+traceData/maxVal, [j for j in range(sampleNum)], color='black', linewidth=lWidth)
        for a in range(len(traceData)):
            if(traceData[a] < 0):
                traceData[a] = 0
        ax.fill(i+traceData/maxVal, [j for j in range(sampleNum)], 'k', linewidth=0)
    ax.axis([0,traceNum,sampleNum,0])
    plt.show()
