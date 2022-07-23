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
    EOF = False
    i = 1
    while EOF == False:
        fileContent = f"{i:02}" + file.read(2)
        hideData = f"{i:02}"

        if len(fileContent) != 2:

            if len(fileContent) == 3:
                fileContent += " "
                
        else:
            fileContent += "\0"
            EOF = True

        # Send to server using created UDP socket
        hideData = fileContent.encode()                 # encode data

        # make the checksum stuff

        # Send the data
        UDPClientSocket.sendto(hideData, serverAddressPort)
        print ("Sending: " + fileContent)

        i += 1



# Receive server response and print
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: " + msgFromServer[0].decode()

print(msg)
