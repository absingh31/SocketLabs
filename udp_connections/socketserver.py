import socket

def main():
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_ip = "127.0.0.1"

	server_port = 15370

	mysocket.bind((server_ip, server_port))

	clientdata, addr = mysocket.recvfrom(153700)

	print(clientdata.decode())

	print("Address of the client : ", addr)

	to_send = "Hey this is server side!!".encode()

	mysocket.sendto(to_send, addr)

	mysocket.close()


if __name__ == "__main__":
	main()