import smtplib
import getpass
import os
import sys
import time
from email.mime.multipart import * 
from email.mime.text import *
from email.mime.image import *
from email.mime.application import *
from plot import plot_graph



def email(host, trafficDataList,interval):
	#This function generates and sends an email to the given recipient
	#using the input taken as parameters
	smtpObj = smtplib.SMTP(host='smtp.office365.com', port=587)
	smtpObj.starttls()
	smtpObj.login('duytt@ntnu.no', password=getpass.getpass(prompt='Enter your password:'))


	msg = MIMEMultipart()
	msg['Subject'] = "tlaffic flow "
	msg['From'] = 'duytt@stud.ntnu.no'
	msg['To'] = 'duytt@stud.ntnu.no'
	
	#This loop generates plots for all trafficData elements in the trafficDataList
	for i in range(0,len(host)):
		graph=plot_graph(host[i],time.time(),trafficDataList[i].getTrafficList(),interval)
		img_data = open(graph, 'rb').read()
		
		image = MIMEImage(img_data, name=os.path.basename(graph))
		msg.attach(image)	

	#This is the text that will be displayed in the email
	text = "Host: "+host[0]+"\n\tip received last "+str(interval*len(trafficDataList[0].getTrafficList()))+" seconds : "+str(trafficDataList[0].getSumOfTrafficList())+" packets\n"+"Host: "+host[1]+"\n\tip received last "+str(interval*len(trafficDataList[1].getTrafficList()))+" seconds : "+str(trafficDataList[1].getSumOfTrafficList())+" packets"
	
	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	#This is where the email is sent
	smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
	smtpObj.quit()
