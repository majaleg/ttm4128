import time
from pysnmp.entity.rfc3413.oneliner import ntforg, cmdgen #moduler fra pysnmp
from moving_window_List_14 import *


#129.241.209.8

ntfOrg = ntforg.NotificationOriginator()
cmdGen = cmdgen.CommandGenerator()
HOST = 'localhost'
THRESHOLD = 19000 #5Mbps youtube 1080p i 15 min, skal generere 5-10 traps, Faen dette er ikke riktig.......
INTERVAL = 5 


def get_datagrams(host='localhost', ipv6=False):
#def get_datagrams(host):

    """
    SNMP GET-forespørsel, returnerer respons eller feilmelding.
    Henter her IP-MIB::ipInReceives og IP-MIB::ipInDelivers
    http://pysnmp.sourceforge.net/docs/current/apps/sync-command-generator.html
    """
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData('ttm4128'),
        cmdgen.UdpTransportTarget((host, 161)),
        #http://www.net-snmp.org/docs/mibs/IP-MIB.txt
        cmdgen.MibVariable('IP-MIB', 'ipInReceives', 0),
        cmdgen.MibVariable('IP-MIB', 'ipInDelivers', 0),
        lookupNames=True, lookupValues=True
    )
    ip_rec = varBinds[0][1]
    ip_del = varBinds[1][1]
    return ip_rec, ip_del

def send_trap(ip_delivered, ip_received, host='localhost'):
    """
    Sender trap til host med siste lesing av verdiene ip_received og ip_delivered, hentet fra get_datagrams
    http://pysnmp.sourceforge.net/docs/current/apps/sync-notification-originator.html
    """
    ntfOrg.sendNotification(
        ntforg.CommunityData('ttm4128'),
        ntforg.UdpTransportTarget((host, 162)),
        'trap',
        ntforg.MibVariable('NTNU-NOTIFICATION-MIB', 'anotif'),
        (ntforg.MibVariable('IP-MIB', 'ipInReceives'), ip_received),
        (ntforg.MibVariable('IP-MIB', 'ipInDelivers',), ip_delivered)
    )


if __name__ == '__main__':
    initReceived, initDel = get_datagrams(HOST)
    makeTrafficList(10,int(format(initReceived)))
    while True:
        ip_received, ip_delivered = get_datagrams('129.241.209.16')#get_datagrams(HOST)
        updateTrafficList(int(format(ip_received)))
        print(getTrafficList())
        print(getSumOfTrafficList())
        sumWindow=getSumOfTrafficList()
        if sumWindow > THRESHOLD:
            send_trap(ip_received, ip_delivered, HOST)
            print('IP RECEIVED: {}'.format(ip_received))
            print('IP DELIVERED: {}'.format(ip_delivered))
        time.sleep(INTERVAL)
