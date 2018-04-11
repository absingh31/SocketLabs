import socket

def main():
	host = '127.0.0.1'

	port = 7890

	s = socket.socket()

	message = input("Enter something to send : ").encode()

	while message != 'q':
		s.send(message)

		data = s.recv(1024)

		print("Received this from the server : " + str(data))

		message = input("Enter the message you want to send : ").encode()

	s.close()


if __name__ == '__main__':
	main()

