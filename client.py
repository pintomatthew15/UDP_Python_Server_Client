import socket
import time
import sys


 

msgFromClient       = "Sample Message, Hello everyone!"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

file_name = sys.argv[1]



 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(file_name, serverAddressPort)
print ("Sending %s ...", file_name)

 

f = open(file_name, "r")
data = f.read(bufferSize)
while(data):
    if (UDPClientSocket.sendto(data, (serverAddressPort))):
        data = f.read(bufferSize)
        time.sleep(0.02) # This gives the receiver time to save


UDPClientSocket.close()
f.close()

