import socket
import codecs
import random
import checksum

ran = random.Random()
ran.seed(3)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
path = "a.txt"
bin_data = open(path, 'rb').read()
hex_data = codecs.encode(bin_data, "hex_codec")

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(('', 5000))
print(UDPClientSocket)
length = len(hex_data)
while len(hex_data) > 0:
    # Open and read the file content
    #with open(file_name, "r") as file:
    send_data = hex_data[0]
    hex_data = hex_data[1:]
    data = ""
    for i in range(0, 500):
        data += chr(random.randint(0, 255))
    print(data, "\n")
    fileContent = checksum.createpacket(send_data, len(hex_data), "127.0.0.1", 20001, "127.0.0.1", 5000, data)
    data = fileContent.encode()     # encode data

    # Send to server using created UDP socket
    UDPClientSocket.sendto(data, serverAddressPort)
    print ("Sending: " + fileContent)



# Receive server response and print
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: " + msgFromServer[0].decode()

print(msg)


