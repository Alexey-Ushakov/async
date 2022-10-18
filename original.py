import socket
from select import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

to_monitor = []

def accept(server_socket):
    print('accept socket')
    conn, addr = server_socket.accept()
    print('Connection from : ', addr)
    to_monitor.append(conn)

def reccive(conn):
    request = conn.recv(1024)
    print(request)
    if request:
        print('We send response')
        response = 'Hello'.encode()
        conn.send(response)
    else:
        conn.close()
        print('Connect is lost')

def event_loop():
    while True:
        read, write, errors = select(to_monitor, [], [])

        for r in read:
            if r is server_socket:
                accept(r)
            else:
                reccive(r)

if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
