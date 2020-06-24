import socket
import select
import sys

def main():
    hostname = 'localhost'
    port = 1025
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((hostname, port))
    server_socket.listen(1)

    client_sockets = []

    while True:
        rlist_input = [server_socket, sys.stdin]
        rlist_input.extend(client_sockets)
        # this will block untill one of the sockets in rlist has input that can be read using
        # recv WITHOUT blocking
        print('blocking on select', [x.fileno() for x in rlist_input])
        rlist_output, _, _ = select.select(rlist_input, [], [])
        print(' resuming on select', [x.fileno() for x in rlist_input])
        connection, client_address = server_socket.accept()

        for s in rlist_output:
            if s == server_socket:
                print('accepted connection')
                connection, client_address = server_socket.accept()
                client_sockets.append(connection)
            elif s == sys.stdin:
                msg = input()
                if msg == 'exit':
                    break
            else:
                print('processing connection',s.fileno())
                msg = s.recv(1024)
                msg = msg.decode()
                s.send(msg.encode())

    server_socket.close()

if __name__ == '__main__':
    main()