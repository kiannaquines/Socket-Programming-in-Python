import socket
import logging
import threading

logger = logging.getLogger(__name__)
logging.basicConfig(filename='crowd_monitoring.log', level=logging.INFO)

DISCONNECT_MESSAGE = 'stop'

def handle_incoming_client(connection,address):
    CONNECTED = True

    logger.info(f"[NEW ACTIVE CONNECTION] New active connection from {address}")
    print(f"[ACTIVE CONNECTION] Connection from {address}")

    while CONNECTED:
        data = connection.recv(1024)

        if not data:
            logger.warning(f"[INVALID MESSAGE RECIEVED] Invalid message recieved from {address}")
            CONNECTED = False
            break

        if data.decode('utf-8') == 'stop':
            CONNECTED = False
            break

        print(data.decode('utf-8'))
        connection.send(b'{accuracy_score:89,f1_score: 90,precision_score:90,time: 10:24 AM}')

    logger.info(f"[CLOSE CONNECTION] Connection from {address} has been terminated")

    print(f"[CLOSE CONNECTION] Connection from {address} has been terminated")
    connection.close()

def start_thread(sock_conn,address):
    print(f"Server is listening to {address}....")
    connection, address = sock_conn.accept()
    incoming_client = threading.Thread(target=handle_incoming_client,args=(connection,address))
    incoming_client.start()

def main(address):
    crowd_monitoring_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    crowd_monitoring_socket.bind(address)
    crowd_monitoring_socket.listen()

    while True:
        start_thread(sock_conn=crowd_monitoring_socket,address=address)
        logger.info(f'[STARTING] Crowd Monitoring Server is starting in {address}')
        logger.info(f'[STARTED] Crowd Monitoring Server is listening to {address}')

if __name__ == "__main__":
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 8090
    ADDRESS = (IP,PORT)
    main(address=ADDRESS)

