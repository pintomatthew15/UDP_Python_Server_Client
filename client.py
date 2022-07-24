import base64
import cv2
import imutils
import socket

from checksum import getPacket

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostname()
host_ip = "127.0.0.1"  # socket.gethostbyname(host_name)
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
file_name = "message.txt"
fileBuffer = []

with open(file_name, "r") as file:
    EOF = False
    while EOF == False:

        fileContent = file.read(2)

        if len(fileContent) != 0:

            if len(fileContent) == 1:
                fileContent += " "

        else:
            fileContent += "##"
            EOF = True

        fileBuffer.append(fileContent)

# vid = cv2.VideoCapture(0)  # replace 'rocket.mp4' with 0 for webcam

vid = cv2.VideoCapture("ZoomData.mp4")  # replace 'rocket.mp4' with 0 for webcam

fps, st, frames_to_count, cnt = (0, 0, 20, 0)

while True:
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ', client_addr)
    WIDTH = 400
    count = 0
    while (vid.isOpened()):
        _, frame = vid.read()
        frame = imutils.resize(frame, width=WIDTH)
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)

        if count > len(fileBuffer) - 1:
            input = hex(0)
        else:
            input = fileBuffer[count]
        hideData = getPacket(input.encode().hex(), count, message.hex())  # encode data

        sendData = bytes.fromhex(hideData)


        server_socket.sendto(sendData, client_addr)


        count += 1
