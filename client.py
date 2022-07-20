import asyncio
import socket
import time
import sys


 

msgFromClient       = "I am The Bad Batch!"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

file_name = sys.argv[1]

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Open and read the file content
with open(file_name, "r") as file:
    fileContent = file.read()
    data = fileContent.encode()     # encode data

    # Send to server using created UDP socket
    UDPClientSocket.sendto(data, serverAddressPort)
    print ("Sending: " + fileContent)



# Receive server response and print
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: " + msgFromServer[0].decode()

print(msg)
