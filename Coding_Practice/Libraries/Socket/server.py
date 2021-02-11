import socket
import threading

# pick port that is not being used anywhere else
PORT = 5050 

# 192.168.1.19
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# create a socket for AF_INET (IPv4) addresses
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    # handle a new connection to the server
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # input how many bytes you want to receive from client
        # we CANNOT move past this line until we receiver information
        # this is WHY it is important to run these in different threads -
        #   so we don't block other clients!
        msg = conn.recv()

def start():
    # start listening for new connection
    server.listen() 
    while True:
        # get port and IP addr of the connection
        conn, addr = server.accept()
        # pass that connection to handle client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # and start that thread
        thread.start()

        # subtract one because our start method thread is always running
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start()