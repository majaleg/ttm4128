import time
from pysnmp.entity.rfc3413.oneliner import ntforg, cmdgen #modules from pysnmp
from moving_window_List_14 import *
from plot import plot_graph1_4, readTrapLog #tused to plot the graph 

#Variables used in the class are all given here
ntfOrg = ntforg.NotificationOriginator()
cmdGen = cmdgen.CommandGenerator()
HOST = 'localhost'
THRESHOLD = 100
INTERVAL = 5 
windowSize = 1000

def get_datagrams(host='localhost', ipv6=False):
    #SNMP GET-request, returns response or error.
    #http://pysnmp.sourceforge.net/docs/current/apps/sync-command-generator.html
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData('ttm4128'),
        cmdgen.UdpTransportTarget((host, 161)),
        #http://www.net-snmp.org/docs/mibs/IP-MIB.txt
        #Gets IP-MIB::ipInReceives and IP-MIB::ipInDeliverscmdgen.MibVariable('IP-MIB', 'ipInReceives', 0),
        cmdgen.MibVariable('IP-MIB', 'ipInDelivers', 0),
        lookupNames=True, lookupValues=True
    )
    ip_rec = varBinds[0][1]
    ip_del = varBinds[1][1]
    return ip_rec, ip_del

def send_trap(ip_delivered, ip_received, host='localhost'):
    #Sends a trap to the host with the last reading of the values ip_received and ip_delivered, retrieved from get_datagrams
    #http://pysnmp.sourceforge.net/docs/current/apps/sync-notification-originator.html
    ntfOrg.sendNotification(
        ntforg.CommunityData('ttm4128'),
        ntforg.UdpTransportTarget((host, 162)),
        'trap',
        ntforg.MibVariable('NTNU-NOTIFICATION-MIB', 'anotif'),
        (ntforg.MibVariable('IP-MIB', 'ipInReceives'), ip_received),
        (ntforg.MibVariable('IP-MIB', 'ipInDelivers',), ip_delivered)
    )


if __name__ == '__main__':
    #Main function
    initReceived, initDel = get_datagrams(HOST)
    makeTrafficList(windowSize,int(format(initReceived)))
    while True:
        ip_received, ip_delivered = get_datagrams(HOST)
        updateTrafficList(int(format(ip_received)))
        print(getTrafficList())
        print(getSumOfTrafficList())
        #Gets the gathered sum of the current trafficList window
        sumWindow=getSumOfTrafficList()
        if sumWindow > THRESHOLD:
            #If the sum has reached the threshold, send a trap message
            send_trap(ip_received, ip_delivered, HOST)
            print('IP RECEIVED: {}'.format(ip_received))
            print('IP DELIVERED: {}'.format(ip_delivered))
            plot_graph1_4(readTrapLog())
        #Wait for [interval] nuumber of seconds
        time.sleep(INTERVAL)
