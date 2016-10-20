import smtplib
import getpass
from email.mime.multipart import * 
from email.mime.text import * 

smtpObj = smtplib.SMTP(host='smtp.office365.com', port=587)
smtpObj.starttls()
smtpObj.login('duytt@ntnu.no', password=getpass.getpass(prompt='Enter your password:'))


def email():
	#template = env.get_template('email.html')
	#text = template.render(traffic_data=traffic_data
	msg = MIMEText('allo from the other side',_subtype='html')
	msg['Subject'] = 'Traffic data'
	msg['From'] = 'duytt@stud.ntnu.no'
	msg['To'] = 'duytt@stud.ntnu.no'
	try:
		#s = smtplib.SMTP('smtp.office365.com') 
	    smtpObj.sendmail('duytt@stud.ntnu.no', 'duytt@stud.ntnu.no', msg.as_string())
	    print("The email was sent!")
	except smtplib.SMTPException:
	    print("Error: unable to send email" + smtplib.SMTPExeption)

email()
