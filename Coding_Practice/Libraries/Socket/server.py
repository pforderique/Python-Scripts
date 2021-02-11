import socket
import threading


HEADER = 64     # length of message that we are receiving (in bytes)
PORT = 5050     # pick port that is not being used anywhere else
SERVER = socket.gethostbyname(socket.gethostname()) # 192.168.1.19
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

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
        msg_length = conn.recv(HEADER).decode(FORMAT) # decode msg from byte format to string

        # use msg length to now accurately get how many bytes we are going to receive 
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}") 

    conn.close()

def start():
    # start listening for new connection
    server.listen() 
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        # get port and IP addr of the connection
        conn, addr = server.accept()
        print(type(conn), type(addr))
        # pass that connection to handle client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # and start that thread
        thread.start()

        # subtract one because our start method thread is always running
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start()