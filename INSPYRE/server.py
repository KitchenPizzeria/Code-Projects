import socket
from socket import gethostbyname
import threading

HEADER = 64
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (HOST,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

server = socket.socket()
server.bind((HOST,PORT))

def Start():
	server.listen(1)
	print(f"[LISTENING] server is on {HOST}")
	while True:
		c, addr = server.accept()
		thread = threading.Thread(target=ClientHandling,args=(c,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

def ClientHandling(conn,addr):
	print(f"[NEW CONNECTION] from {addr}")

	while True:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		msg_length = int(msg_length)
		msg = conn.recv(msg_length).decode(FORMAT)
		print(f"[{addr}] {msg}")
		if msg == DISCONNECT_MESSAGE:
			break 
	
	conn.close()

print("[STARTING] server is starting...")
Start()

