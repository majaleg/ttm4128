from send_mail import email
from snmpclient import get_datagrams 
from moving_window_List import *
from plot import plot_graph
import time

#Variables used in the class are all given here
running=0
agentHosts = ('129.241.209.16','129.241.209.8')   
mailInterval = 5*60
sampleInterval= 5
windowSize = 1000
trafficDataList = [0,0]
i = 0
threshold = 15000
timeSinceLastMail=0

#Calls the email function (is given in this file for readability)
def sendMail():
	email(agentHosts, trafficDataList,sampleInterval)

#Creates one trafficData object in trafficDataList for every given host in agentHosts 
for agentHost in agentHosts:
	trafficDataList[i] = trafficData()
	i += 1


if __name__ == '__main__':
	#This is the main function that will monitor the packages sent
	#The email with this gathered data will be sent every [mailInterval] seconds
	#Ex: mailInterval = 5*60 --> Sends an email every 5 minutes
	timeSinceLastMail=time.time()		
	while True:
		timer = time.time()

		for agent in range(0,2):
			#This loop runs over all given agents in agentHosts and gets the data needed
			ip_rec, ip_del = get_datagrams(agentHosts[agent])
			if running <2:
				#If this is the first iteration, a trafficList is made, and the windowSize is defined.
				#To ensure that the initial difference stored in the trafficList is not equal
				#to the number of packages sent since the computer connected to the internet, 
				#the inital value stored is 0
				trafficDataList[agent].makeTrafficList(windowSize,int(format(ip_rec)))
				running += 1				
			print(format(ip_rec))
			#Here the data list is updated with the data downloaded within the timeframe [sampleInterval]
			trafficDataList[agent].updateTrafficList(int(format(ip_rec)))
			
			#If it has been [mailInterval] seconds since the last email, send an email
			if timeSinceLastMail+mailInterval<time.time():
				print("send MAIL")
				timeSinceLastMail=time.time()
				sendMail()
		#Wait for [sampleInterval] seconds and repeat
		time.sleep(sampleInterval)	

