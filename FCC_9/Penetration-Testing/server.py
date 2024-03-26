import socket
import threading #a way to create multiple threads in one python program for messaging

PORT = 5050
#inet 192.168.1.74  netmask 255.255.255.0  broadcast 192.168.1.255
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64 # how many bytes a message needs to be
FORMAT  = 'utf-8' # decoding purposes
DISCONNECT = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("NEW Connection: {}".format(addr))
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # receive how many bytes the message is receiving
        msg_length = int(msg_length) # turn that into an int
        message = conn.recv(msg_length).decode(FORMAT) # decode actual message

        if message == DISCONNECT:
            connected = False

        print("{}: {}".format(addr, message))

    conn.close()

def start():
    server.listen()
    print("LISTENING on {}".format(SERVER))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("ACTIVE Connections: {}".format(threading.activeCount() - 1))

print("STARTING Connection")
start()