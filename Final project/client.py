import socket
import termcolor
from Seq2 import Seq
class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        pass

    def __str__(self):
        return f"Connection to SERVER at {self.IP}, PORT: {self.PORT}"

    def ping(self):
        print(termcolor.colored("Ping Command!", "blue"))

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.IP, self.PORT))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response