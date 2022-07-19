import socket
import select

 

localIP= "127.0.0.1"

localPort= 20001

bufferSize=1024

timeout= 3

 

msgFromServer= "Hello UDP Client"

bytesToSend= str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    if bytesAddressPair:
        print ("File name", bytesAddressPair)
        file_name = bytesAddressPair.strip()
    f = open(file_name, 'wb')

    while True:
        ready = select.select([UDPServerSocket], [], [], timeout)
        if ready[0]:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            f.write(bytesAddressPair)
        else:
            print("%s Finish!", file_name)
            f.close()
            break
