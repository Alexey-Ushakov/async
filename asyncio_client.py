import asyncio


class EchoClientProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
        response = 'hello'.encode()
        print(response)
        self.transport.write(response)

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        self.transport.write('hello'.encode())


    def start_server(self):
        loop = asyncio.get_event_loop()
        coro = loop.create_connection(EchoClientProtocol, '127.0.0.1', 8888)
        client = loop.run_until_complete(coro)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        # Close the server
        client.close()
        loop.run_until_complete(client.wait_closed())
        loop.close()


client = EchoClientProtocol()
client.start_server()
