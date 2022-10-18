import asyncio


class EchoServerClientProtocol(asyncio.Protocol):
    # def __init__(self, host: str, port: int):
        # self.host = host
        # self.port = port
    def __init__(self):
        self.clients = []

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
        response = 'hello'.encode()
        print(response)
        self.transport.write(response)
        self.clients.append(self.transport)


    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        response = 'hello'.encode()
        print(response)
        self.transport.write(response)

    def connection_lost(self, exc):
        print('Connection lost')

    def start_server(self):
        loop = asyncio.get_event_loop()
        coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
        server = loop.run_until_complete(coro)

        # Serve requests until Ctrl+C is pressed
        print('Serving on {}'.format(server.sockets[0].getsockname()))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        # Close the server
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()


server = EchoServerClientProtocol()
server.start_server()
