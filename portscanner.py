import socket
import subprocess
import sys
from datetime import datetime
import errno

subprocess.call('clear',shell=True)

remote_server = input('Enter the domain name: ')
remote_server_IP=socket.gethostbyname(remote_server)

print('IPv4',remote_server_IP)

print("-"*60)
print('please wait while scanning', remote_server_IP)
print("-"*60)

t1=datetime.now()

try:
    for port in range(79,885):
        connexion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        resultat=connexion.connect_ex((remote_server_IP,port))

        if resultat == 0:
            print('port{}: open'.format(port))

        else:
            print('port{}: close'.format(port))

        connexion.close()

except KeyboardInterrupt:
    print('You pressed Crtl+C !!')
    sys.exit()

except:
    print('something wrong')
    sys.exit()

t2=datetime.now()

Ttotal=t2+t1
print('-'*60)
print('scan done in',Ttotal,'second')