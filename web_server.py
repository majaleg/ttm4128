from flask import Flask, render_template
from cim_client import *
from snmpclient import get_snmp_os, get_snmp_interface


app = Flask(__name__)

#url/endpoint for loading page: usually localhost:PORT/<<app.route(link)>>
#@app.route("/cim_info")
#e.g. http://127.0.0.1:5000/cim_info
#def hello():
#        return render_template('cim.html')



#-------------- CIM Section -----------------------------------
@app.route("/cim_info")
def get_cim_info():
	os = get_OS_info()

	#get appropriate interface data from cim_client and format it
	interfaces = formatIP(get_ip_interfaces())
	return render_template('cim.html', os=os, interfaces=interfaces)


#-------------- END CIM Section --------------------------------





#-------------- SNMP Section -----------------------------------
@app.route("/snmp_info")
def get_snmp_info():
	os = get_snmp_os()
	interfaces = formatIP(get_snmp_interface())
	print(formatIP(get_snmp_interface()))
	return render_template('snmp.html', os=os, interfaces=interfaces)


#-------------- END SNMP Section -------------------------------


#Formats output from interfaces
def formatIP(interfaces):
	outputString="<p>"
	for interface in interfaces:
		outputString+="<b>Name: </b>" + interface['name']+"<br>"
		outputString+="<b>IP: </b>" + interface['ip_address']+"<br>"
		outputString+="<b>Network mask: </b>" + interface['subnet_mask']+"<br>"
		outputString+="<br>"
	return outputString


@app.route("/")
def index():
	return render_template('layout.html')

if __name__ == "__main__":
            app.run(debug=True)
