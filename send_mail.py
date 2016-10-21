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
	smtpObj = smtplib.SMTP(host='smtp.office365.com', port=587)
	smtpObj.starttls()
	#smtpObj.login('duytt@ntnu.no', password=getpass.getpass(prompt='Enter your password:'))
	smtpObj.login('duytt@ntnu.no', 'proCrastinate420')
	#template = env.get_template('email.html')
	#text = template.render(traffic_data=traffic_data

	msg = MIMEMultipart()
	#msg = MIMEText('allo from the other side',_subtype='html')
	msg['Subject'] = "tlaffic flow "
	msg['From'] = 'duytt@stud.ntnu.no'
	msg['To'] = 'duytt@stud.ntnu.no'

	for i in range(0,len(host)):
		graph=plot_graph(host[i],time.time(),trafficDataList[i].getTrafficList(),interval)
		img_data = open(graph, 'rb').read()
		
		image = MIMEImage(img_data, name=os.path.basename(graph))
		msg.attach(image)	


	text = "Host: "+host[0]+"\n\tip received last "+str(interval*len(trafficDataList[0].getTrafficList()))+" seconds : "+str(trafficDataList[0].getSumOfTrafficList())+" packets\n"+"Host: "+host[1]+"\n\tip received last "+str(interval*len(trafficDataList[1].getTrafficList()))+" seconds : "+str(trafficDataList[1].getSumOfTrafficList())+" packets"

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)


	smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
	smtpObj.quit()
