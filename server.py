import socket
import select

from checksum import getChecksum

 

localIP= "127.0.0.1"

localPort= 20001

bufferSize=1024

timeout= 3

hideDataBuf = ""

 

msgFromServer= "Hello The Bad Batch"

bytesToSend= str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams
while(True):


    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0].decode()

    address = bytesAddressPair[1]

    # clientMsg = "Message from Client: " + message
    # clientIP  = "Client IP Address: {}".format(address)
    
    hideData = getChecksum(message)    # Recover the hided data
    # print(hideData)
    hideSequ = hideData[:2]             # Recover the hided sequence
    # print(hideSequ)
    hideMsg = hideData[2:]              # Revocer the hided message
    # print(hideMsg)

    # Store message in our buffer
    hideDataBuf += hideMsg.decode()
    print(hideDataBuf)

    if hideData == b'00\x00':
        print("EOF")
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
        hideDataBuf = ""
