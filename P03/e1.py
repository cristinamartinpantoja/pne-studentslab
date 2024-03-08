import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('212.128.255.37', 8081)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on {}:{}".format(*server_address))

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()

        # Receive data from the client
        request = client_socket.recv(2048).decode('utf-8').strip()

        # Check if the received message is a PING command
        if request == "PING":
            print("PING command!")

            # Generate the response message
            response = "\033[0mOK!\n"  # ANSI escape code for white color

            # Print the response message in white
            print(response)

            # Send the response to the client
            client_socket.send(response.encode('utf-8'))
        else:
            print(f"Unknown command received: {request}")

        # Close the client socket
        client_socket.close()
        print(f"Connection from {client_address} closed")

        server_socket.close()


start_server()