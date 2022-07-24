# Client Program to be run to send covert data to server.py

import base64
import cv2
import socket

from checksum import getPacket

# initial setup
BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostname()
host_ip = "127.0.0.1"
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
file_name = "message.txt"
fileBuffer = []

# read in covert data
with open(file_name, "r") as file:
    EOF = False
    while not EOF:

        fileContent = file.read(2)

        if len(fileContent) != 0:

            if len(fileContent) == 1:
                fileContent += " "

        else:
            fileContent += "##"
            EOF = True

        fileBuffer.append(fileContent)

# read in zoom data
vid = cv2.VideoCapture("ZoomData.mp4")  # replace "ZoomData.mp4" with 0 for webcam

# change and send packets
while True:
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ', client_addr)
    WIDTH = 400
    count = 0
    while vid.isOpened():
        _, frame = vid.read()
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)

        if count > len(fileBuffer) - 1:
            covertInput = hex(0)
        else:
            covertInput = fileBuffer[count]
        hideData = getPacket(covertInput.encode().hex(), count, message.hex())  # encode data

        sendData = bytes.fromhex(hideData)

        server_socket.sendto(sendData, client_addr)

        count += 1
