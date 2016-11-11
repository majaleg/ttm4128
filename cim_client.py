import pywbem 

conn = pywbem.WBEMConnection('http://ttm4128.item.ntnu.no:5988')
print "hello"
processes = conn.EnumerateInstances('CIM_Process')
print processes[0].items()





