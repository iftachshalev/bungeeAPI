import socket
from Messages import StartGameMessage


class Translator:

    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.client_socket = None
        self.address = None

    def connect(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.client_socket, self.address = self.server_socket.accept()

    def dis_connect(self):
        pass

    def receive(self):
        data = self.client_socket.recv(1024)
        dec_message = StartGameMessage()
        data_in_array = dec_message.decode(data).array


    def send(self):
        pass
