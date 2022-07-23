import asyncio
import socket
import time
import sys

from checksum import createpacket


RandData = '10000000000000000000000000000001110000000000000000000000000000011000000000000000000000000000000111000000000000000000000000000001'

msgFromClient       = "I am The Bad Batch!"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

file_name = sys.argv[1]

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Open and read the file content
with open(file_name, "r") as file:
    EOF = False
    i = 1
    while EOF == False:
        fileContent = file.read(2)

        if len(fileContent) != 0:

            if len(fileContent) == 1:
                fileContent += " "
                
        else:
            fileContent += "\0"
            i = 0
            EOF = True

        # Send to server using created UDP socket
        hideData = createpacket(fileContent, i, RandData)                 # encode data

        # make the checksum stuff

        # Send the data
        UDPClientSocket.sendto(hideData, serverAddressPort)
        print ("Sending: " + str(hideData))

        i += 1



# Receive server response and print
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: " + msgFromServer[0].decode()

print(msg)
