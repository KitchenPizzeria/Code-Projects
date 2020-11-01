import socket
import pickle
import time

def Main():

	HEADER = 40000
	HOST = socket.gethostbyname(socket.gethostname())
	PORT = 5005
	ADDR = (HOST,PORT)
	FORMAT = "utf-8"

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(ADDR)

	print("[CONNECTED] Connection Successful\n[SENDING] 'Test Message' is being sent to server ...")
	time.sleep(2)
	

	raw_dict = {"name": "Joseph", "Surname": "Meyrick"}
	msg = pickle.dumps(raw_dict)
	s.send(bytes(msg))
	print("[SENT] Test Dictionary has been sent")

	raw_data = s.recv(10240)
	print(f"debug: receeived data is {raw_data}")
	data = pickle.loads(raw_data)
	#data = pickle.load(raw_data)
	#data = raw_data.decode(FORMAT)
	time.sleep(2)
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
