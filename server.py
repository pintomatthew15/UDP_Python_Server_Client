# This is server code
import base64
import time

import cv2
import numpy as np
import socket

from checksum import getChecksum

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostname()
host_ip = "127.0.0.1"
port = 9999
message = b'0'

hideDataBuf = {}

client_socket.sendto(message, (host_ip, port))
while True:
    packet, _ = client_socket.recvfrom(BUFF_SIZE)
    try:
        data = base64.b64decode(packet + b'=' * (3 - len(packet) % 4), ' /')
        npdata = np.fromstring(data, dtype=np.uint8)
        frame = cv2.imdecode(npdata, 1)
        cv2.imshow("RECEIVING VIDEO", frame)
        key = cv2.waitKey(1) & 0xFF

    except:
        pass

    hiddenData = getChecksum(packet.hex())  # Recover the hidden data
    hiddenData = ''.join(hiddenData)
    hideSeq = hiddenData[:16]
    hideMsg = hiddenData[16:]
    binary_int = int(hideMsg, 2)
    byte_number = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    hideDataBuf[int(hideSeq, 2)] = ascii_text
    print("Packet Recived", ascii_text)

    if ascii_text == "##":
        print("EOF")
        f = open("recivedMessage.txt", "w")
        for i in range(0, len(hideDataBuf)):
            try:
                f.write(hideDataBuf[i])
            except:
                print("index", i, "lost")

        f.close()

        # open and read the file after the appending:
        f = open("recivedMessage.txt", "r")
        print(f.read())
