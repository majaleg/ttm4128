import pywbem 
#PyWBEM represents CIM objects in a generic way.
conn = pywbem.WBEMConnection('http://ttm4128.item.ntnu.no:5988/cimom')


#Gets OS Version
def get_OS_info():
	os = conn.EnumerateInstances('CIM_OperatingSystem')[0]
	os_version = os['Version']
	#print os_version
	return os_version

#Get Interface info: name, ipaddress and network mask
def get_ip_interfaces():
	interface_info=[]
	interfaces = conn.EnumerateInstances('CIM_IPProtocolEndpoint')
	#print interfaces.items()
	for interface in interfaces:
		print interface['Name']+interface['ipv4address']+interface['subnetmask']
		interface_info.append({
			'name':		interface['Name'],
			'ip_address':	interface['ipv4address'],
			'subnet_mask':	interface['subnetmask']
		}) 		
	return interface_info


get_OS_info()



