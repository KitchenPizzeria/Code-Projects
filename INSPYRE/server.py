import socket
import pickle

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5005
ADDR = (HOST,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

print("[STARTING] server is starting...")

server = socket.socket()
server.bind((HOST,PORT))
server.listen(4)

print(f"[LISTENING] server is on {HOST}")

while True:
	conn, addr = server.accept()
	print(f"[NEW CONNECTION] from {addr}")

	pickled_msg = conn.recv(1024)
	msg = pickle.loads(pickled_msg)
	print(f"[RECEIVED] Received from client: {msg}")

	raw_reply = dict(msg).update({"Age": 21})
	print(raw_reply)
	reply = pickle.dumps(raw_reply)
	print(f'[DEBUG] reply = {reply}')
	conn.send(bytes(reply))
	print(f"[RETURNED] Edits made and dictionary has been returned")
	conn.close()




