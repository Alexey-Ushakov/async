import socket
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen(0)


def accept():
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection from: ', addr)
        Thread(target=reccive, args=(client_socket, )).start()


def reccive(client_socket):
    while True:
        request = client_socket.recv(1024)
        if request:
            response = 'Hello'.encode()
            client_socket.send(response)
        else:
            client_socket.close()
            print('Connection lost')


Thread(target=accept).start()

