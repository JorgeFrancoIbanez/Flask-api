import os


def get_mac():
    try:
        for i in os.listdir('/sys/class/net/'):
            operstate = open('/sys/class/net/%s/operstate' %i).read()
            if operstate == 'up' and i == 'eth0' or i == 'enp0s31f6':
                mac_address = open('/sys/class/net/%s/address' %i).read()
                return str(mac_address[0:17])
    except ValueError:
        print 'Please check your available connections before continuing'