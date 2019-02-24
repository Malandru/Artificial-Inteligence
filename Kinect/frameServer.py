import SocketServer
import pickle
import numpy as np
import demo_cv_sync as kinect

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)
        #print "{} wrote:".format(self.client_address[0])
        frame = kinect.get_video()
        self.send(frame)

    def send(self, data):
        #conversion of an np.array to string
        data = data.flatten()
        data = data.tostring()
        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 2000

    # Create the server, binding to localhost on port 2000
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

"""
para decodificar
lista = numpy.fromstring(self.data, dtype=int)
print lista[0]
"""