import socket
class Client:
    def __init__(self, IP, PORT):

        self.IP = IP
        self.PORT = PORT

    def ping(self):

        response = "OK!"
        print(response)

    def __str__(self):

        return "Connection to SERVER at " + self.IP + ", PORT:" + str(self.PORT)



    # talk method in the Client class
    def talk(self, msg):
        print(f"Connecting to {self.IP}:{self.PORT}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.IP, self.PORT))
            # rest of the code...
        except Exception as e:
            print(f"Error connecting to the server: {e}")
        finally:
            s.close()


