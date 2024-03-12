import socket

PORT = 8081
IP = "212.128.255.28"

while True:
    #Ask the user for a message
    user_message = input("Enter your message")

    #Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Establish the connection to the sever
    s.connect((IP , PORT))

    #Send the user message
    s.sendall(user_message.encode("utf-8"))

    #Close the socket
    s.close()