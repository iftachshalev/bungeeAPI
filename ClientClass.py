import socket
from Messages import StartGameMessage
import threading
import time


class Client:

    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.client_socket = None
        self.address = None
        self.dict = dict()
        self.data_in_array = None

    def connect(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.client_socket, self.address = self.server_socket.accept()

    def dis_connect(self):
        pass

    def receive(self):
        data = self.client_socket.recv(1024)
        self.data_in_array = StartGameMessage.decode(data).array

    def send(self):
        pass

    def arrange_dict(self):
        self.dict["State"] = self.data_in_array[0]
        if self.dict["State"] == 1:
            self.dict["PlayerNumber"] = self.data_in_array[1]
            self.dict["Cards"] = self.data_in_array[2]
            self.dict["LuckyCard"] = self.data_in_array[3]
            self.dict["LastPlayer"] = self.data_in_array[4]
        if self.dict["State"] == 2:
            pass


def hello():
    print("hello, Timer")


if __name__ == '__main__':

    t = threading.Timer(3.0, hello)
    t.start()
    while True:
        pass
