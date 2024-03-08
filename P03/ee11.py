from Seq1 import Seq
import socket

class SeqServer:
    def __init__(self, port):
        self.port = port
        self.server_socket = None


    def start_server():
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to a specific address and port
        server_address = ('212.128.255.37', 8081)
        server_socket.bind(server_address)

    def seq_ping(self):
        print("Testing the seq_ping function")
        print("OK!")