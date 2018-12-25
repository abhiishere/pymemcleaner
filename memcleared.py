print("this module is a memory cleaner(only for upto 16GB RAM devices as of now)")
# importing the necessary modules
import psutil
import sys
try :
    import psutil
except ImportError:
    print("download psutil from pip")
# conversions of some units of memory
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
# pre cleanup statistics
memory=(psutil.virtual_memory()._asdict())
freemem=unitconvertMB(memory["free"])
usedmem=unitconvertMB(memory["used"])
totalmem=unitconvertMB(memory["total"])
platform=(sys.platform).lower()
installedmem=unitconvertGB(memory["total"])
percentused=(memory["percent"])
c=usedmem
print("Memory usage statistics before cleanup")
print("current platform",platform.upper())
print("The number of CPU logical cores:",psutil.cpu_count(logical=True)," cores")
print("current CPU frequency :",psutil.cpu_freq(percpu=False),"MHz")
print("The RAM memory used is approx :",round(usedmem),"MB")
print("The RAM memory free is approx :",round(freemem),"MB")
print("The total RAM memory available to system",round(totalmem),"MB")
print("The total capacity of RAM installed",round(installedmem),"GB")
# memory operation mode
if platform=="linux":
    mode={0:320,1:650,2:1760,3:2650,4:3650,6:5450,8:7450,16:15350}
    modechosen=mode[round(installedmem)]
    print("Target attack memory peak:",modechosen)
else :
    mode={0:300,1:650,2:1350,3:2350,4:3600,6:5450,8:7450,16:15350}
    modechosen=mode[round(installedmem)]
    print("Target attack memory peak:",modechosen)
# main code for memory cleaner
x=input("type 123 to begin")
lst1=[]
for A in range(1,1000000) :
                N1=A*x
                lst1.append(N1)
                memory=(psutil.virtual_memory()._asdict())
                freemem=unitconvertMB(memory["free"])
                usedmem=unitconvertMB(memory["used"])
                if usedmem>=modechosen:
                        print("memory cleaned successfully")
                        break
                else:
                        pass
#memory usage statistics after memorycleanup
print("memory usage statistics after cleanup")
print("peak memory usage:",usedmem)
z=input("Press enter to exit")
