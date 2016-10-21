from send_mail import email
from snmpclient import get_datagrams 
from moving_window_List import *
from plot import plot_graph
import time

running=0
agentHosts = ('129.241.209.16','129.241.209.8')   
mailInterval = 10
sampleInterval=5
windowSize = 1000
trafficDataList = [0,0]
i = 0
threshold = 15000
timeSinceLastMail=0

def sendMail():
	email(agentHosts, trafficDataList,sampleInterval)


for agentHost in agentHosts:
	trafficDataList[i] = trafficData()
	i += 1

	


if __name__ == '__main__':
	timeSinceLastMail=time.time()
	#makeTrafficList(1000,int(format(ip_rec)))		
	while True:
		timer = time.time()
		i = 0
		'''for agent in agentHosts:
			i	p_rec, ip_del = get_datagrams(agentHosts[agent])
			if running <2:
				trafficDataList[i].makeTrafficList(1000,int(format(ip_rec)))
				running += 1
			else:
				print("shit is running")				
			print(format(ip_rec))
			updateTrafficList(int(format(ip_rec)))
		time.sleep(30)
		if time.time()+10>timer:
			graphname=timer
			traffic = getTrafficList()
			print("NIGGA")
			#reset timer
			timer=time.time()
		'''
		for agent in range(0,2):
			ip_rec, ip_del = get_datagrams(agentHosts[agent])
			if running <2:
				trafficDataList[agent].makeTrafficList(windowSize,int(format(ip_rec)))
				running += 1				
			print(format(ip_rec))
			trafficDataList[agent].updateTrafficList(int(format(ip_rec)))
			
			if timeSinceLastMail+mailInterval<time.time():
				print("send MAIL")
				timeSinceLastMail=time.time()
				sendMail()
		time.sleep(sampleInterval)	
		'''#CHECK getSumOfTrafficList
		if (((timer+10)>time.time())):
			graphname=timer
			traffic = trafficDataList[agent].getTrafficList()
			print("NIGGA")
			time.sleep(2)			
			#reset timer
			#timer=time.time()'''

