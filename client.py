import asyncio
import socket
import codecs
import time
import sys


 

msgFromClient       = "ABCD"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

bin_data = open(path, 'rb').read()
hex_data = codecs.encode(bin_data, "hex_codec")

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(('', 5000))
print(UDPClientSocket)
 
# Open and read the file content
#with open(file_name, "r") as file:
fileContent = msgFromClient
data = fileContent.encode()     # encode data

# Send to server using created UDP socket
UDPClientSocket.sendto(data, serverAddressPort)
print ("Sending: " + fileContent)



# Receive server response and print
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: " + msgFromServer[0].decode()

print(msg)


