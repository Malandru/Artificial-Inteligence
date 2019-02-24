import socket
import pickle
import sys
import numpy as np

HOST, PORT = "localhost", 2000
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = ''

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    data = raw_input()
    sock.sendall(data.encode('ascii'))
    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

"""
#conversion de string a numpyArray
data = np.fromstring(data, dtype=int)
"""
received = np.fromstring(received, dtype=int)

print ("Sent: ", data)
print ("Received: ", received)