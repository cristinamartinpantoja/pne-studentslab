import socket
from Seq1 import Seq

    def ping_request(message):
        if message == "PING":
            print("PING command!")
            response = "OK!\n"
            return response
        else:
            return "Invalid command\n"


    def start_server():
        IP = "212.128.255.37"
        PORT = 8080

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((IP, PORT))
        server_socket.listen(1)

        print(f"Server listening on {IP}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            message = client_socket.recv(2048).decode('utf-8').strip()
            print(f"Received request: {message}")

            response = ping_request(message)

            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()


        start_server()



