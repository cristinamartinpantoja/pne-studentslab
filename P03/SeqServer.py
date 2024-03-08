import socket
from Seq1 import Seq

class SeqServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")

            message = client_socket.recv(1024).decode('utf-8').strip()

            if message.startswith("GENE"):
                try:
                    _, gene_name = message.split()
                    print(f"GENE command for gene {gene_name}!")

                    # Read gene sequence from the file using the Seq class
                    gene_filename = f"../sequences/{gene_name}"
                    with open(gene_filename, 'r') as gene_file:
                        gene_sequence = gene_file.read().strip()

                    client_socket.send(f"Gene {gene_name}: {gene_sequence}\n".encode('utf-8'))
                except ValueError:
                    print("Invalid GENE command format!")
                    client_socket.send("Invalid GENE command format\n".encode('utf-8'))

            client_socket.close()

server = SeqServer('127.0.0.1', 8080)
server.start()