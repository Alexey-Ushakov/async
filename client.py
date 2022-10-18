import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))

def send_msg():
    while True:
        try:
            name = input('your name: ')  # write
            client_socket.send(name.encode())
            data = client_socket.recv(1024) # read
            msg = data.decode()
            print(msg)
        except ConnectionError:
            print('connection close')
            break

