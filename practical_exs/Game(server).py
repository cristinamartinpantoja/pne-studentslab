import socket
import random
class Server:
    def __init__(self):
        port = 8080
        ip = "127.0.0.1"
        secret_number  = random.randint(1, 100).

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((ip, port))
            # become a server socket
            serversocket.listen()
            print("Server configured!")
            while True:
                # accept connections from outside
                print("\nWaiting for clients...")
                (clientsocket, address) = serversocket.accept()

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")
                # Send the message from the server
                clientsocket.send(msg)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(ip, port))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    class NumberGuesses():

        def __int__(self, secret_number):
            self.secret_number = secret_number
        def guess(self, secret_number):
            guessing = True
            while guessing:
                attempt = int(input('Enter an integer : '))
                if attempt == secret_number:
                    print('Congratulations, you guessed it.')
                    guessing = False
                elif attempt < secret_number:
                    print("No, I'm afraid it is a little higher than that.")

                else:
                    print("No, I'm afraid it is a little lower than that.")

s = Server()
