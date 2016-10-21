import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as date
import re




#Converts from seconds to date
def secondsToDate(sec):
	return date.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')


## 1.4
def readTrapLog():
	trapLog = open("/home/tin/.snmp/log.txt", "r+")
	lines = trapLog.readlines()
	
	ip_received=[]
		
	for line in lines:
		pattern = re.compile("(IP-MIB::ipInReceives = Counter32: )(\d+)")
		datagrams = pattern.search(str(line))
		
		if datagrams:
			print(datagrams.group(2))
			ip_received.append(datagrams.group(2))
	return ip_received



#Plots the array input
#Generate the plot using the graph "timestamp"
def plot_graph1_4(array): 
    x = [i for i in range(len(array))]

    plt.plot(x, array)
    plt.xlabel('måling nummer')
    plt.ylabel('antall pakker i denne perioden')
    plt.title("Output i trap loggen")
    plt.grid(True)

    filename="output_trapd_log.png"
    plt.savefig(filename)
    plt.show()
    plt.close("all")



##  1.5
def plot_graph(host,timestamp, array, INTERVAL): 
    timestampAkse = [0 for i in range(len(array))]
    x = [i for i in range(len(array))]
    #Generates the time values for the x-axis of the graph based on when the threshold time has been reached
    for i in range(0,len(array)):
        timestampAkse[i]=secondsToDate(timestamp-(len(array)-(i+1))*INTERVAL)

    #plt.xticks(x, timestampAkse)
    plt.plot(x, array)
    plt.xlabel('måling nummer')
    plt.ylabel('antall pakker i denne perioden')
    plt.title(host)
    plt.grid(True)
    filename=secondsToDate(timestamp)+".png"
    plt.savefig(filename)
    plt.close("all")
    return filename

