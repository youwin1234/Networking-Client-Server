import socket

def main():
    hostname = 'localhost'
    port = 1025

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hostname, port))

    while True:
        msg = input('<<')
        print('sending')
        client_socket.send(msg.encode())
        print('receiving')
        msg2 = client_socket.recv(1024)
        print(msg2.decode())
    client_socket.close()

if __name__ == '__main__':
    main()