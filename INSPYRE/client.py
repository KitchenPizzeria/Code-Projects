import socket

def Main():
	host = "127.0.0.1"
	port = 5000

	s = socket.socket()
	s.connect((host,port))

	msg = input("-> ")
	while msg != "q":
		s.send(bytes(msg))
		data = s.recv(1024)
		print(f"Received from server: {str(data)}")
		msg = input("-> ")

	s.close()
		
	

if __name__ == "__main__" :
	Main()
