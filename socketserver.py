import socket 

def main():
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host_ip = "127.0.0.1"   # my device address

	host_port = 15370		# any random port

	mysocket.bind(host_ip, host_port)	

	mysocket.listen(5)     # backlog in default documentation page , you can take any value other than 5

	(client, (ip, host_port)) = mysocket.accept()

	client.send("Hey!! server this side : ".encode())

	data = client.recv(2048).decode()   # 2048 bytes of data received at a time

	print(data)

	mysocket.close()


if __name__ == "__main__":
	main()