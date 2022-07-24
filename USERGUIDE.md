# UDP_Python_Server_Client
By Annan McGlade, Sarah Chalokh, and Matthew Pinto 

## Installation Instructions

### Required Software
1. Python v 3.8.10
2. Python Socket Library v 3.10.5
3. Python cv2 Library v 4.6.0.66


### Install
1. Clone this repository with the command  ```git clone https://github.com/pintomatthew15/UDP_Python_Server_Client.git```
2. install dependency ```cv2``` library with the following commands:
- ```pip install opencv-python```


## Running the Server and Client
1. Open two seperate terminals (one for the client and another for the server)
2. Run the client server first with the command: ```python3 client.py```
3. Run the server next with the command: ```python3 server.py```


### About Our Solution
Our solution takes traffic generated from an infected UDP application, like Zoom, and modifies the UDP packet's data section to contain our hidden data. The packets travel over the network like normal network traffic and the data is saved in the server. Therefore, our covert message appears like any other data over the server and remains undetected. 


