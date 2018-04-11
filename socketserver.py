import socket

def main():
	host = "127.0.0.1"
	port = 7890

	s = socket.socket()

	s.bind((host, port))

	s.listen(1)

	c, addr = s.accept()

	print("Connection from : " + str(addr) + "and c is : " + str(c))

	while True:
		data = c.recv(1024)   #number of bytes you wanna receive at one time

		if not data:
			break

		print("We got this from the connected user : " + str(data))

		print("Sending the acknowledgement : ")

		to_send = "We received from you, thanks!!!".encode()
		c.send(to_send)

	c.close()


if __name__ == '__main__':
	main()