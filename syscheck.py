# a program to monitor system statistics
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import psutil
#array initialization for monitor plot
memtime=np.array([])
memused=np.array([])
memfree=np.array([])
#some unit conversion functions
def MB():
    x=1024**2
    return x
def GB():
    y=1024**3
    return y
def unitconvertMB(z):
    c=MB()
    d=z/c
    return d
def unitconvertGB(z):
    c=GB()
    d=z/c
    return d
# Create plot
plt.figure(figsize=(10,7))
style.use('ggplot')
plt.ion()
plt.show()

while True:
    #memory use details
    memory=(psutil.virtual_memory()._asdict())
    freemem=unitconvertMB(memory["free"])
    usedmem=unitconvertMB(memory["used"])
    totalmem=unitconvertMB(memory["total"])
    installedmem=unitconvertGB(memory["total"])
    percentused=(memory["percent"])
    newtime=(time.clock())/60
    memtime=np.append(memtime,newtime)
    memfree=np.append(memfree,freemem)
    memused=np.append(memused,usedmem)
    #memory plot
    plt.clf()
    plt.plot(memtime,memused,linewidth=3,color="Red")
    plt.plot(memtime,memfree,linewidth=3,color="Blue")
    plt.ylabel('Memory (MB)')
    plt.xlabel('Time (m)')
    plt.title("RAM memory Status")
    plt.draw()
    plt.pause(0.05)

        
