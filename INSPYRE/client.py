import socket
import pickle

def Main():

	HEADER = 40000
	HOST = socket.gethostbyname(socket.gethostname())
	PORT = 5000
	ADDR = (HOST,PORT)
	FORMAT = "utf-8"

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(ADDR)

	d = {"name":"Joseph","Surname":"Meyrick"}
	msg = pickle.dumps(d)

	print("[CONNECTED] Connection Successful\n[SENDING] Test dict is being sent to server ...")
	
	s.send(msg)
	print(f"[SENT] Dictionary has been sent")
	data = s.recv(1024)
	print(f"[RECEIVED] Received from server: {data}")

	s.close()


	# msg = input("message: ")
	# while msg != "q":
	# 	s.send(bytes(msg))
	# 	data = s.recv(1024)
	# 	print(f"Received from server: {str(data)}")
	# 	msg = input("-> ")

	# s.close()
		
	

if __name__ == "__main__" :
	Main()
