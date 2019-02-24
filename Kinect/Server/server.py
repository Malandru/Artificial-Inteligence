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
        serialized_data = pickle.dumps(data, protocol=2)
        self.request.sendall(serialized_data)

if __name__ == "__main__":
    HOST, PORT = "192.168.0.65", 2000

    # Create the server, binding to localhost on port 2000
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print 'Service is up'
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

"""
para decodificar
lista = numpy.fromstring(self.data, dtype=int)
print lista[0]
"""