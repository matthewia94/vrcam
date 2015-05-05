import SocketServer

class UDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        socket.sendto(data.upper(), self.client_address)
        
