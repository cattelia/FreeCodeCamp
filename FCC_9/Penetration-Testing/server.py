import socket
import threading #a way to create multiple threads in one python program for messaging

PORT = 5050
#inet 192.168.1.74  netmask 255.255.255.0  broadcast 192.168.1.255
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("NEW CONNECTION: {}".format(addr))
    connected = True
    while connected:
        message = conn.recv()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("ACTIVE Connections: {}".format(threading.activeCount() - 1))

print("")
start()