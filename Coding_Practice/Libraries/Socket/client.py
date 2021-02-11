import socket

HEADER = 64     # length of message that we are receiving (in bytes)
PORT = 5050     # pick port that is not being used anywhere else
SERVER = socket.gethostbyname(socket.gethostname()) # 192.168.1.19 # use this if on another device!
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 

def send(msg):
    message = msg.encode(FORMAT) # encodes string into byte like object
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) 
    send_length += b' '*(HEADER - len(send_length)) # b returns byte representation 
    client.send(send_length)
    client.send(message)

if __name__ == "__main__":
    send("hello there!")
    send(DISCONNECT_MESSAGE)
