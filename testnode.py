import argparse
import requests
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

parser = argparse.ArgumentParser(description='Add user to the database.')
parser.add_argument('--email', type=str, default='jorgefrancoibanez@gmail.com', help='Password to be hashed')
parser.add_argument('--name', type=str, default='pc', help='name of the node')
args = parser.parse_args()

r = requests.post('http://127.0.0.1:5000/users', data=args.email)
print r.content
data = {'email': args.email,
        'mac': get_mac(),
        'name': args.name}

url = 'http://127.0.0.1:5000/nodes/{}'.format(str(r.content).rstrip())
r = requests.post(url=url, json=data)

print r.content