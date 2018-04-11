import socket

def main():
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_ip = "127.0.0.1"

	server_port = 15370

	mysocket.connect((server_ip, server_port))

	data = mysocket.recv(2048).decode()

	print(data)

	mysocket.send("This is from the client side!!".encode())

	mysocket.close()

if __name__ == "__main__":
	main()