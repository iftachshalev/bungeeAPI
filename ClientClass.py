import socket
from Messages import StartGameMessage
import threading
import time


class Client:

    PACK_LEN = 1024
    TO_QUIT = b"Q"

    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.client_socket = None
        self.address = None
        self.dict = dict()
        self.data_in_array = None
        self.sen_message = None
        self.state = "disconnect"

    def connect(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.client_socket, self.address = self.server_socket.accept()
        self.state = "connect"

    def disconnect(self):
        if self.state == "connect":
            self.client_socket.sendall(self.TO_QUIT)
            self.server_socket.close()
            self.client_socket.close()

    def receive(self):
        data = self.client_socket.recv(self.PACK_LEN)
        self.data_in_array = StartGameMessage.decode(data).array
        self.arrange_dict()
        return self.dict

    def send(self, throw, get, bungee):
        if bungee:
            self.sen_message = StartGameMessage(throw, get, bungee)
        else:
            self.sen_message = StartGameMessage(throw, get)
        self.client_socket.sendall(self.sen_message.encode())

    def arrange_dict(self):
        self.dict["State"] = self.data_in_array[0]
        if self.dict["State"] == 1:
            self.dict["PlayerNumber"] = self.data_in_array[1]
            self.dict["Cards"] = self.data_in_array[2]
            self.dict["LuckyCard"] = self.data_in_array[3]
            self.dict["LastPlayer"] = self.data_in_array[4]
        if self.dict["State"] == 2:
            self.dict["LastPlayer"] = self.data_in_array[1]
            self.dict["BungeeMode"] = self.data_in_array[2]
        if self.dict["State"] == 3:
            self.dict["PlayerNumber"] = self.data_in_array[1]
        if self.dict["State"] == 4:
            self.dict["Score"] = self.data_in_array[1]


def hello():
    print("hello, Timer")


if __name__ == '__main__':

    t = threading.Timer(3.0, hello)
    t.start()
    while True:
        pass
