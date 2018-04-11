import socket

def main():
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_ip = "127.0.0.1"

	server_port = 15370

	mysocket.connect((server_ip, server_port))

	message = "This is client side ".encode()

	mysocket.sendto(message, (server_ip, server_port))

	data, add_recived = (mysocket.recvfrom(2048))

	print(data.decode())

	mysocket.close()


if __name__ == "__main__":
	main()