import socket
import json
import time

IP = '192.168.226.1'
PORT = int(8090)
ADDRESS = (IP,PORT)

crowd_monitoring_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
crowd_monitoring_socket.connect(ADDRESS)

disconnect_msg = b'0x00'

for i in range(10):
    message = 'Sending {i}: {message}'.format(i=i,message='message from kian').encode('utf-8')
    crowd_monitoring_socket.send(message)
    time.sleep(2)
    data_recieved = crowd_monitoring_socket.recv(1024)
    data = json.dumps(data_recieved.decode('utf-8'))
    print(data)

crowd_monitoring_socket.send(disconnect_msg)
crowd_monitoring_socket.close()